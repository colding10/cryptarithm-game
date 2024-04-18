"""This module defines Tkinter-derived classes that are used to control the GUI and user input"""

import tkinter
import tkinter.font
import tkinter.messagebox
import textwrap

from string import ascii_uppercase

CHARS_IN_ROW = 40
BGCOLOR = "dark gray"
FGCOLOR = "light gray"
TEXTCOLOR = "black"


class App(tkinter.Tk):
    """This class is a subclass of tkinter.Tk, and contains functions to set up the Tk interface"""
    def __init__(self):
        super().__init__()

        self.title("Cryptarithms by Colin Ding")
        self.geometry(f"{1100}x{580}")
        self.config({"bg": BGCOLOR})

        self.text_frame = tkinter.Frame(self, bg=BGCOLOR)
        self.text_frame.pack(fill="both", side="top", expand=True, padx=5, pady=5)

        self.freq_table_frame = tkinter.Frame(self, bg=BGCOLOR)
        self.freq_table_frame.pack(side="bottom", expand=True, padx=5, pady=5)

        # Initialize list to hold labels and input spaces
        self.labels = []
        self.input_spaces = []
        self.freq_table_labels = [[None for _ in range(27)] for _ in range(3)]
        self.input_string = ""

        print("Initalized Tkinter Application")

    def display_string_with_input(self, input_string: str):
        for label in self.labels:
            label.destroy()
        for input_space in self.input_spaces:
            input_space.destroy()

        self.labels = []
        self.input_spaces = []

        self.input_string = input_string

        # Create labels and input spaces for each character in the input string
        lines = textwrap.wrap(input_string, CHARS_IN_ROW, break_long_words=False)

        for row_index, row in enumerate(lines):
            for col_index, char in enumerate(row):
                # Create label for character
                label = tkinter.Label(
                    self.text_frame,
                    text=char,
                    font=("FiraMono Nerd Font", 24),
                    bg=BGCOLOR,
                )
                label.grid(row=row_index * 2, column=col_index, sticky="nsew")
                self.labels.append(label)

                # If character is a letter, create input space
                if char.isalpha():

                    def focus_in_handler(event, c=char):
                        self.on_focus_in(event, c)

                    def key_pressed_handler(event, c=char):
                        typed_char = event.char.upper()
                        curridx = self.input_spaces.index(event.widget)
                        if event.keysym_num == 65288:
                            for input_space in self.input_spaces:
                                if (
                                    isinstance(input_space, tkinter.Entry)
                                    and input_space.cget("bg") == "yellow"
                                ):
                                    input_space.delete(0, "end")

                            event.widget.delete(0, "end")

                            self.freq_table_labels[2][
                                ascii_uppercase.index(c) + 1
                            ].config({"text": ""})
                            return "break"

                        if event.keysym_num == 65363:
                            for i in range(curridx + 1, len(self.input_spaces)):
                                if not isinstance(self.input_spaces[i], tkinter.Entry):
                                    continue
                                self.input_spaces[i].focus_set()
                                return "break"
                        if event.keysym_num == 65361:
                            for i in range(curridx - 1, -1, -1):
                                if not isinstance(self.input_spaces[i], tkinter.Entry):
                                    continue
                                self.input_spaces[i].focus_set()
                                return "break"
                        if typed_char.isalpha():
                            event.widget.delete(0, "end")
                            event.widget.insert("end", typed_char)

                            for input_space in self.input_spaces:
                                if (
                                    isinstance(input_space, tkinter.Entry)
                                    and input_space.cget("bg") == "yellow"
                                ):
                                    input_space.delete(0, "end")
                                    input_space.insert("end", typed_char)

                            for i in range(
                                curridx + 1, len(self.input_spaces)
                            ):  # TODO: make it go back to beginning if none after
                                if not isinstance(self.input_spaces[i], tkinter.Entry):
                                    continue
                                if not self.input_spaces[i].get().isalpha():
                                    self.input_spaces[i].focus_set()
                                    break

                            self.freq_table_labels[2][
                                ascii_uppercase.index(c) + 1
                            ].config({"text": typed_char})

                        return "break"

                    input_space = tkinter.Entry(
                        self.text_frame,
                        width=1,
                        font=("FiraMono Nerd Font", 24),
                        bg=FGCOLOR,
                        fg=TEXTCOLOR,
                        justify="center",
                    )

                    input_space.bind("<FocusIn>", focus_in_handler)
                    input_space.bind("<Key>", key_pressed_handler)

                    input_space.grid(
                        row=(row_index * 2) + 1, column=col_index, sticky="nsew"
                    )

                    self.input_spaces.append(input_space)
                else:
                    self.input_spaces.append(None)

    def setup_frequency_table(self, freqs: dict[str, int]):
        table = [["" for _ in range(27)] for _ in range(3)]
        table[1][0] = "Frequency"
        table[2][0] = "Replacement"

        for i, let in enumerate(ascii_uppercase):
            table[0][i + 1] = let

        for i, let in enumerate(ascii_uppercase):
            table[1][i + 1] = str(freqs[let] if freqs[let] else "")

        for i in range(3):
            for j in range(27):
                e = tkinter.Label(
                    self.freq_table_frame,
                    text=table[i][j],
                    width=2 if j else 11,
                    bg=BGCOLOR,
                    fg=TEXTCOLOR,
                    font=("FiraMono Nerd Font", 22, "bold"),
                    anchor=tkinter.CENTER if j else tkinter.E,
                    borderwidth=1,
                    relief="solid",
                    padx=1,
                    pady=1,
                )

                e.grid(row=i, column=j, sticky="nsew")
                e.bind("<Button-1>", self.on_freq_label_pressed)
                self.freq_table_labels[i][j] = e

    def on_freq_label_pressed(self, event: tkinter.Event):
        widget = event.widget
        idx = -1
        for i in range(3):
            if widget in self.freq_table_labels[i]:
                idx = self.freq_table_labels[i].index(widget) - 1

        if idx == -1:
            raise Exception("check sanity please")

        char_to_hl = ascii_uppercase[idx]

        for i, lbl in enumerate(self.labels):
            if lbl.cget("text") == char_to_hl:
                self.input_spaces[i].focus_set()

    def on_focus_in(self, event: tkinter.Event, bound_char: str = ""):
        for inp in self.input_spaces:
            if isinstance(inp, tkinter.Entry):
                inp.config({"bg": "light gray"})

        for i, inp in enumerate(self.input_spaces):
            if (
                self.labels[i].cget("text").strip().upper()
                == bound_char.strip().upper()
            ):
                inp.config({"bg": "yellow"})

        event.widget.config({"bg": "orange"})


if __name__ == "__main__":
    app = App()
    app.display_string_with_input(
        "SAMPLESTRING PEOPLE ANYWHERE IS THE" * 5
    )  # Replace "Sample String" with desired input
    app.mainloop()
