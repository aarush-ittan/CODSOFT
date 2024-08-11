import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x250")

        # Create UI elements
        self.label1 = tk.Label(root, text="Enter first number:", font=("Arial", 12))
        self.label1.pack(pady=10)

        self.entry1 = tk.Entry(root, font=("Arial", 12))
        self.entry1.pack(pady=5)

        self.label2 = tk.Label(root, text="Enter second number:", font=("Arial", 12))
        self.label2.pack(pady=10)

        self.entry2 = tk.Entry(root, font=("Arial", 12))
        self.entry2.pack(pady=5)

        self.label3 = tk.Label(root, text="Choose operation:", font=("Arial", 12))
        self.label3.pack(pady=10)

        self.operation = tk.StringVar()
        self.operation.set("+")  # Default value

        self.operation_menu = tk.OptionMenu(root, self.operation, "+", "-", "*", "/")
        self.operation_menu.pack(pady=5)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate, font=("Arial", 12))
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            op = self.operation.get()

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
            else:
                messagebox.showerror("Error", "Invalid operation")
                return

            self.result_label.config(text=f"Result: {result}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
