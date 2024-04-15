from gui import *
from cipher import *


if __name__ == "__main__":
    cipher = CipherAristocrat()
    user_mapping = dict(zip(ascii_uppercase, " " * 26))

    app = App()
    app.display_string_with_input(cipher.cipher_text)
    app.mainloop()
