"""This module uses the rich library to create a cli. NOT IN USE"""

from string import ascii_uppercase

from rich.console import Console
from rich.table import Table

from cipher import CipherAristocrat, CipherMonoSub

console = Console()
SOLVED = True


def output_frequency_table(cip: CipherMonoSub) -> None:
    """Outputs a rich-formatted table with the frequency table"""
    table = Table(show_lines=True)

    table.add_column("", style="bold black")
    for char in ascii_uppercase:
        table.add_column(char, style="magenta", justify="center", min_width=2)

    table.add_row("Frequency", *[str(x) if x else "" for x in cip.frequency.values()])
    table.add_row("Replacement", *user_mapping.values())

    console.print(table, justify="center")


def output_cipher_plaintext(cip: CipherMonoSub) -> None:
    """Outputs the cipher's plaintext in the cli"""
    console.print(cip.cipher_text, justify="center")
    console.print(
        "".join(
            [user_mapping[c] if c in ascii_uppercase else c for c in cip.cipher_text]
        ),
        justify="center",
        end="",
        style=("bold green" if SOLVED else ""),
    )


def mainloop() -> None:
    """Runs the loop for user input"""
    console.clear()
    global SOLVED
    while True:
        try:
            output_cipher_plaintext(cipher)
            console.print("\n\n")
            console.print(cipher.plain_text)
            output_frequency_table(cipher)
            inp = input()
            a, b = inp.split("=")
            user_mapping[a.upper()] = b.upper()
            console.clear()

            if (
                "".join(
                    [
                        user_mapping[c] if c in ascii_uppercase else c
                        for c in cipher.cipher_text
                    ]
                )
                == cipher.plain_text
            ):
                SOLVED = True
        except KeyboardInterrupt:
            return


cipher = CipherAristocrat()
user_mapping = dict(zip(ascii_uppercase, " " * 26))

mainloop()
