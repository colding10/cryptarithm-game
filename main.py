"""This module generates the cipher and feeds it to the GUI. Mainloop is in this module"""

from string import ascii_uppercase

import cipher
import gui

if __name__ == "__main__":
    cipher = cipher.CipherAristocrat()
    print(cipher.plain_text)
    user_mapping = dict(zip(ascii_uppercase, " " * 26))

    app = gui.App()
    app.display_string_with_input(cipher.cipher_text)
    app.setup_frequency_table(cipher.frequency)
    app.mainloop()
