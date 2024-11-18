import tkinter as tk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Input field
        self.expression = ""
        self.input_text = tk.StringVar()
        input_frame = tk.Frame(self.root, bd=5)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 18), bd=5, insertwidth=4, justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10, fill=tk.BOTH)

        # Button frame
        btns_frame = tk.Frame(self.root, bg="grey")
        btns_frame.pack()

        # Layout of buttons
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', 'x²',
            '0', '.', '%', '+', '=',
            '←', '^'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            btn = tk.Button(btns_frame, text=button, font=('Arial', 18), fg='black', width=5, height=2, bd=1, command=lambda b=button: self.button_click(b))
            btn.grid(row=row_val, column=col_val, padx=1, pady=1)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def button_click(self, button):
        if button == "C":
            self.expression = ""
            self.input_text.set("")
        elif button == "←":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif button == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set("")
        elif button == "√":
            try:
                result = str(math.sqrt(float(self.expression)))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                messagebox.showerror("Error", "Invalid Input for Square Root")
                self.expression = ""
                self.input_text.set("")
        elif button == "x²":
            try:
                result = str(float(self.expression) ** 2)
                self.input_text.set(result)
                self.expression = result
            except Exception:
                messagebox.showerror("Error", "Invalid Input for Square")
                self.expression = ""
                self.input_text.set("")
        elif button == "%":
            try:
                result = str(float(self.expression) / 100)
                self.input_text.set(result)
                self.expression = result
            except Exception:
                messagebox.showerror("Error", "Invalid Input for Percentage")
                self.expression = ""
                self.input_text.set("")
        elif button == "^":
            self.expression += "**"
            self.input_text.set(self.expression)
        else:
            self.expression += str(button)
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()