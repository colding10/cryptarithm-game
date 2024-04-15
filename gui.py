import tkinter
import tkinter.font
import tkinter.messagebox


ROWS = 40


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cryptarithms by Colin Ding")
        self.geometry(f"{1100}x{580}")

        self.text_frame = tkinter.Frame(self)
        self.text_frame.pack(fill="both", side="right", expand=True)

        # Initialize list to hold labels and input spaces
        self.labels = []
        self.input_spaces = []
        self.input_string = ""

    def display_string_with_input(self, input_string: str):
        for label in self.labels:
            label.destroy()
        for input_space in self.input_spaces:
            input_space.destroy()

        self.labels = []
        self.input_spaces = []

        self.input_string = input_string

        # Create labels and input spaces for each character in the input string
        for i, char in enumerate(input_string):
            col_index = i % ROWS
            row_index = i // ROWS

            # Create label for character
            label = tkinter.Label(self.text_frame, text=char, font=("FiraMono Nerd Font", 24))
            label.grid(row=row_index * 2, column=col_index, sticky="nsew")
            self.labels.append(label)

            # If character is a letter, create input space
            if char.isalpha():

                def focus_in_handler(event, c=char):
                    self.on_focus_in(event, c)

                def key_pressed_handler(event, c=char):
                    typed_char = event.char.upper()
                    curridx = self.input_spaces.index(event.widget)

                    if event.keysym_num == 65363:
                        for i in range(curridx + 1, len(self.input_spaces)):
                            if not isinstance(self.input_spaces[i], tkinter.Entry):
                                continue
                            if not self.input_spaces[i].get().isalpha():
                                self.input_spaces[i].focus_set()
                                return "break"
                    if event.keysym_num == 65361:
                        for i in range(curridx - 1, -1, -1):
                            if not isinstance(self.input_spaces[i], tkinter.Entry):
                                continue
                            if not self.input_spaces[i].get().isalpha():
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

                    return "break"

                input_space = tkinter.Entry(
                    self.text_frame,
                    width=1,
                    font=("FiraMono Nerd Font", 24),
                    bg="light gray",
                    fg="black",
                    justify="center"
                )

                input_space.bind("<FocusIn>", focus_in_handler)
                input_space.bind("<Key>", key_pressed_handler)

                input_space.grid(
                    row=(row_index * 2) + 1, column=col_index, sticky="nsew"
                )

                self.input_spaces.append(input_space)
            else:
                self.input_spaces.append(None)

    def on_focus_in(self, event: tkinter.Event, bound_char: str = ""):
        for inp in self.input_spaces:
            if isinstance(inp, tkinter.Entry):
                inp.config({"bg": "light gray"})

        for i in range(len(self.input_spaces)):
            if (
                self.labels[i].cget("text").strip().upper()
                == bound_char.strip().upper()
            ):
                self.input_spaces[i].config({"bg": "yellow"})

        event.widget.config({"bg": "orange"})


if __name__ == "__main__":
    app = App()
    app.display_string_with_input(
        "SAMPLESTRING PEOPLE ANYWHERE IS THE" * 5
    )  # Replace "Sample String" with desired input
    app.mainloop()
