"""This module uses the rich library to create a cli. NOT IN USE"""

from string import ascii_uppercase

from rich.console import Console
from rich.table import Table

from cipher import CipherAristocrat, CipherMonoSub


def output_frequency_table(console: Console, cip: CipherMonoSub, user_mapping) -> None:
    """Outputs a rich-formatted table with the frequency table"""
    table = Table(show_lines=True)
    table.add_column("", style="bold black")
    for char in ascii_uppercase:
        table.add_column(char, style="magenta", justify="center", min_width=2)

    table.add_row("Frequency", *[str(x) if x else "" for x in cip.frequency.values()])
    table.add_row("Replacement", *user_mapping.values())

    console.print(table, justify="center")


def output_cipher_plaintext(console: Console, cip: CipherMonoSub, user_mapping) -> bool:
    """Outputs the cipher's plaintext in the cli"""
    console.print(cip.cipher_text, justify="center")
    console.print(
        "".join(
            [user_mapping[c] if c in ascii_uppercase else c for c in cip.cipher_text]
        ),
        justify="center",
        end="",
        style=("bold green" if is_solved(cip, user_mapping) else ""),
    )
    return is_solved(cip, user_mapping)


def mainloop() -> None:
    """Runs the loop for user input"""
    console = Console()
    console.clear()
    cip = CipherAristocrat()
    user_mapping = dict(zip(ascii_uppercase, " " * 26))

    while True:
        try:
            output_cipher_plaintext(console, cip, user_mapping)
            console.print("\n\n")
            console.print(cip.plain_text)
            output_frequency_table(console, cip, user_mapping)
            inp = input()
            a, b = inp.split("=")
            user_mapping[a.upper()] = b.upper()
            console.clear()

            if is_solved(cip, user_mapping):
                break
        except KeyboardInterrupt:
            return


def is_solved(cip: CipherMonoSub, user_mapping) -> bool:
    """Check if the cipher is solved"""
    return (
        "".join(
            [user_mapping[c] if c in ascii_uppercase else c for c in cip.cipher_text]
        )
        == cip.plain_text
    )


if __name__ == "__main__":
    mainloop()
