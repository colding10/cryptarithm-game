"""This module uses the rich library to create a cli. NOT IN USE"""
from rich.console import Console
from rich.table import Table
from cipher import CipherMonoSub, CipherAristocrat
from string import ascii_uppercase

console = Console()


def output_frequency_table(cipher: CipherMonoSub) -> None:
    table = Table(show_lines=True)

    table.add_column("", style="bold black")
    for char in ascii_uppercase:
        table.add_column(char, style="magenta", justify="center", min_width=2)

    table.add_row(
        "Frequency", *[str(x) if x else "" for x in cipher.frequency.values()]
    )
    table.add_row("Replacement", *user_mapping.values())

    console.print(table, justify="center")


def output_cipher_plaintext(cipher: CipherMonoSub) -> None:
    console.print(cipher.cipher_text, justify="center")
    console.print(
        "".join(
            [user_mapping[c] if c in ascii_uppercase else c for c in cipher.cipher_text]
        ),
        justify="center",
        end="",
        style=("bold green" if solved else ""),
    )


def mainloop() -> None:
    console.clear()

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
                solved = True
        except KeyboardInterrupt:
            return


cipher = CipherAristocrat()
user_mapping = dict(zip(ascii_uppercase, " " * 26))
solved = False

mainloop()
