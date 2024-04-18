"""This module defines popup functions to ask and get user response"""

import tkinter.messagebox as messagebox


WINNING_MESSAGE = (
    """You won! Congratulations on solving the cipher! Would you like to play again?"""
)


def ask_play_again() -> bool:
    """Uses tkinter.messagebox to ask to play again"""
    response = messagebox.askyesno(
        title="Colin's Cryptarithms", message=WINNING_MESSAGE, icon=messagebox.QUESTION
    )
    return response


if __name__ == "__main__":
    print(ask_play_again())
