import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("RPS Best of 5")
        self.user_score = 0
        self.comp_score = 0
        self.round = 0

        self.label = tk.Label(root, text="Round 1 of 5", font=("Arial", 14))
        self.label.pack()

        self.result = tk.Label(root, text="", font=("Arial", 12))
        self.result.pack()

        for c in choices:
            btn = tk.Button(root, text=c, width=10, command=lambda ch=c: self.play_round(ch))
            btn.pack(pady=2)

        self.score = tk.Label(root, text="Your Score: 0 | Computer: 0")
        self.score.pack()

    def play_round(self, user_choice):
        if self.round >= 5:
            return

        comp_choice = random.choice(choices)
        msg = f"Computer chose {comp_choice}. "

        if user_choice == comp_choice:
            msg += "Draw!"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or              (user_choice == "Scissors" and comp_choice == "Paper") or              (user_choice == "Paper" and comp_choice == "Rock"):
            self.user_score += 1
            msg += "You Win!"
        else:
            self.comp_score += 1
            msg += "You Lose!"

        self.round += 1
        self.label.config(text=f"Round {self.round+1 if self.round<5 else 5} of 5")
        self.result.config(text=msg)
        self.score.config(text=f"Your Score: {self.user_score} | Computer: {self.comp_score}")

        if self.round == 5:
            final = "Final Result: "
            if self.user_score > self.comp_score:
                final += "You Won!"
            elif self.user_score < self.comp_score:
                final += "Computer Won!"
            else:
                final += "It's a Tie!"
            self.result.config(text=final)

root = tk.Tk()
game = RPSGame(root)
root.mainloop()
