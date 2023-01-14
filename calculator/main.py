import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("200x250")

        self.result = tk.Entry(self)
        self.result.pack()

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", lambda: self.add_number(7)),
            ("8", lambda: self.add_number(8)),
            ("9", lambda: self.add_number(9)),
            ("+", lambda: self.add_operator("+")),
            ("4", lambda: self.add_number(4)),
            ("5", lambda: self.add_number(5)),
            ("6", lambda: self.add_number(6)),
            ("-", lambda: self.add_operator("-")),
            ("1", lambda: self.add_number(1)),
            ("2", lambda: self.add_number(2)),
            ("3", lambda: self.add_number(3)),
            ("*", lambda: self.add_operator("*")),
            ("C", lambda: self.clear()),
            ("0", lambda: self.add_number(0)),
            ("=", lambda: self.calculate()),
            ("/", lambda: self.add_operator("/")),
        ]

        for index, button in enumerate(buttons):
            tk.Button(self, text=button[0], command=button[1]).pack()

    def add_number(self, number):
        current = self.result.get()
        self.result.delete(0, tk.END)
        self.result.insert(0, str(current) + str(number))

    def add_operator(self, operator):
        current = self.result.get()
        self.result.delete(0, tk.END)
        self.result.insert(0, str(current) + operator)

    def clear(self):
        self.result.delete(0, tk.END)

    def calculate(self):
        current = self.result.get()
        self.result.delete(0, tk.END)
        self.result.insert(0, eval(current))

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
