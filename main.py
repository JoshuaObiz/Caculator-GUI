import tkinter as tk

PRIMARY = '#28cdfb'
GREY = '#aaaeaf'
LABEL_COLOR = '#0e1011'
SMALL_FONT = ('Poppins', 16)
LARGE_FONT = ('Poppins', 32)


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('375x667')
        self.window.resizable(None, None)
        self.window.title("GUI Calculator")

        self.total_expression = '0'
        self.current_expression = '0'
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_label, self.label = self.create_display_labels()

    # CREATED DISPLAY LABELS
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=GREY, fg=LABEL_COLOR,
                               padx=24, font=SMALL_FONT)
        total_label.pack(expand=True, fill='both')
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=GREY, fg=LABEL_COLOR,
                               padx=24, font=LARGE_FONT)
        label.pack(expand=True, fill='both')
        return total_label, label

    # CREATED FRAMES
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=GREY)
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
