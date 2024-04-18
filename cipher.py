"""This module defines the classes for each cipher type"""

from string import ascii_uppercase

from utility import create_alphabet_mapping, get_quote_max_length, QuoteType


class CipherMonoSub:
    """This is the class that encapsulates Aristocrats and Patristocrats,
    every letter decrypts to another letter."""

    quote: QuoteType
    quote_text: str

    plain_text: str
    cipher_text: str
    author: str

    mapping: dict[str, str]
    frequency: dict[str, int]

    def __init__(self) -> None:
        self.quote = get_quote_max_length(160)
        self.quote_text = self.quote["quote"]
        self.plain_text = self.quote["quote"].upper()
        self.author = self.quote["author"]

        print(f"Initalized Cipher with quote of length {len(self.quote_text)}")
        print(f"Got cipher plaintext as {self.plain_text}")
        print(f"This quote is by {self.author}")
        self.create_alphabet_mapping()

    def create_alphabet_mapping(self) -> None:
        """Creates the alphabet mapping using the utility module"""
        self.mapping = create_alphabet_mapping()

    def create_frequency_table(self) -> None:
        """Counts the occurances and creates the freq table"""
        countings = [self.cipher_text.count(char) for char in ascii_uppercase]
        self.frequency = dict(zip(ascii_uppercase, countings))


class CipherAristocrat(CipherMonoSub):
    """This class is a variant of `CipherMonoSub` and it has spaces"""

    def __init__(self) -> None:
        super().__init__()
        self.create_cipher_text()
        self.create_frequency_table()

    def create_cipher_text(self) -> None:
        """Creates the cipher text and preserves non-alpha characters"""
        self.cipher_text = "".join(
            [
                (self.mapping[char] if char in ascii_uppercase else char)
                for char in self.plain_text
            ]
        )


class CipherPatristocrat(CipherMonoSub):
    """This class is a variant of `CipherMonoSub` and it does not have spaces"""

    def __init__(self) -> None:
        super().__init__()
        self.create_cipher_text()
        self.create_frequency_table()

    def create_cipher_text(self) -> None:
        """Creates the cipher text and removes spaces"""
        self.cipher_text = "".join(
            [
                (self.mapping[char] if char in ascii_uppercase else "")
                for char in self.plain_text
            ]
        )
