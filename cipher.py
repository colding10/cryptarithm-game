from utility import *
import random
from string import ascii_uppercase


class CipherMonoSub:
    quote: QuoteType
    quote_text: str

    plain_text: str
    cipher_text: str
    author: str

    mapping: Dict[str, str]
    frequency: Dict[str, int]

    def __init__(self) -> None:
        self.quote = get_quote_max_length(175)
        self.quote_text = self.quote["quote"]
        self.plain_text = self.quote["quote"].upper()
        self.author = self.quote["author"]

        print(f"Initalized Cipher with quote of length {len(self.quote_text)}")
        self.create_alphabet_mapping()

    def create_alphabet_mapping(self) -> None:
        alphabet_reordered = list(ascii_uppercase)
        random.shuffle(alphabet_reordered)

        self.mapping = dict(zip(alphabet_reordered, ascii_uppercase))

    def create_frequency_table(self) -> None:
        countings = [self.cipher_text.count(char) for char in ascii_uppercase]
        self.frequency = dict(zip(ascii_uppercase, countings))


class CipherAristocrat(CipherMonoSub):
    def __init__(self) -> None:
        super().__init__()
        self.create_cipher_text()
        self.create_frequency_table()

    def create_cipher_text(self) -> None:
        self.cipher_text = "".join(
            [
                (self.mapping[char] if char in ascii_uppercase else char)
                for char in self.plain_text
            ]
        )


class CipherPatristocrat(CipherMonoSub):
    def __init__(self) -> None:
        super().__init__()
        self.create_cipher_text()
        self.create_frequency_table()

    def create_cipher_text(self) -> None:
        self.cipher_text = "".join(
            [
                (self.mapping[char] if char in ascii_uppercase else "")
                for char in self.plain_text
            ]
        )
