import tkinter as tk

PRIMARY = '#f5f5f5'
GREY = '#aaaeaf'
LABEL_COLOR = '#0e1011'
WHITE = '#ffffff'
OFF_WHITE = '#f5f5f8'
SMALL_FONT = ('Poppins', 16)
DEFAULT_FONT = ('Poppins', 20)
LARGE_FONT = ('Poppins', 32)
DIGIT_FONT = ('Poppins', 24, 'bold')


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('375x667')
        self.window.resizable(None, None)
        self.window.title("GUI Calculator")

        self.total_expression = ''
        self.current_expression = ''
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '.': (4, 1), 0: (4, 2)
        }
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.operations = {
            '/': '\u00f7', '*': '\u00d7', '-': '-', '+': '+'
        }
        self.create_operator_buttons()
        self.create_square_root_button()
        self.create_square_button()
        self.create_clear_button()
        self.create_equals_button()
        self.create_special_buttons()
        
    # CREATED FRAMES
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=GREY)
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame

    # CREATED DISPLAY LABELS
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=GREY, fg=LABEL_COLOR,
                               padx=24, font=SMALL_FONT)
        total_label.pack(expand=True, fill='both')
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=GREY, fg=LABEL_COLOR,
                         padx=24, font=LARGE_FONT)
        label.pack(expand=True, fill='both')
        return total_label, label

    # CREATED DIGITS
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # CREATED OPERATORS
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text='x\u00b2', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_square_root_button(self):
        button = tk.Button(self.buttons_frame, text='\u221ax', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text='C', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', bg=PRIMARY, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, sticky=tk.NSEW, columnspan=2)

    def create_special_buttons(self):
        self.create_equals_button()
        self.create_clear_button()

    # UPDATE LABELS
    def update_total_labels(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    # EXPRESSION FUNCTIONS
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    # OPERATOR FUNCTION
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.update_total_labels()
        self.update_label()

    # SQUARE FUNCTION
    def square(self):
        self.current_expression = str(eval(f'{self.current_expression}**2'))
        self.update_label()

    # SQUARE ROOT FUNCTION
    def square_root(self):
        self.current_expression = str(eval(f'{self.current_expression}**0.5'))
        self.update_label()

    # CLEAR FUNCTION
    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_total_labels()
        self.update_label()

    #     EVALUATE FUNCTION
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_labels()
        self.current_expression = str(eval(self.total_expression))
        self.total_expression = ''
        self.update_label()

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
