import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x200")

        # Create UI elements
        self.label = tk.Label(root, text="Enter the desired password length:", font=("Arial", 12))
        self.label.pack(pady=20)

        self.length_entry = tk.Entry(root, font=("Arial", 12), width=10)
        self.length_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Arial", 12))
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(root, text="", font=("Arial", 12), wraplength=300)
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Length must be positive.")

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))

            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid positive integer for the password length.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
