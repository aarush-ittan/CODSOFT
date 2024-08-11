import random
import tkinter as tk
from tkinter import messagebox
class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        self.root.geometry("400x300")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        # Create UI elements
        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
        self.label.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.rock_button = tk.Button(root, text="Rock", width=10, command=lambda: self.play("Rock"), font=("Arial", 12))
        self.rock_button.pack(side=tk.LEFT, padx=20)

        self.paper_button = tk.Button(root, text="Paper", width=10, command=lambda: self.play("Paper"), font=("Arial", 12))
        self.paper_button.pack(side=tk.LEFT, padx=20)

        self.scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: self.play("Scissors"), font=("Arial", 12))
        self.scissors_button.pack(side=tk.LEFT, padx=20)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)

        # Update the result label and score
        self.result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}. {result}")
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
