import tkinter as tk
from PIL import Image, ImageTk
import random
import os

print("Current working directory:", os.getcwd())

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.score_label = tk.Label(self.root, text="Scores: You - 0 | Computer - 0", font=("Arial", 16))
        self.score_label.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="Make your choice!", font=("Arial", 14))
        self.result_label.pack(pady=10)
        
        self.user_choice_label = tk.Label(self.root, text="Your choice: ", font=("Arial", 12))
        self.user_choice_label.pack(pady=5)
        
        self.computer_choice_label = tk.Label(self.root, text="Computer's choice: ", font=("Arial", 12))
        self.computer_choice_label.pack(pady=5)

        self.rock_img = Image.open("rock paper scissors\\rock.png")
        self.rock_img = self.resize_image(self.rock_img)
        self.rock_img = ImageTk.PhotoImage(self.rock_img)
        
        self.paper_img = Image.open("rock paper scissors\\paper.png")
        self.paper_img = self.resize_image(self.paper_img)
        self.paper_img = ImageTk.PhotoImage(self.paper_img)
        
        self.scissors_img = Image.open("rock paper scissors\\scissors.png")
        self.scissors_img = self.resize_image(self.scissors_img)
        self.scissors_img = ImageTk.PhotoImage(self.scissors_img)
        
        self.rock_button = tk.Button(self.root, image=self.rock_img, command=lambda: self.play_round("rock"))
        self.rock_button.pack(pady=5, side=tk.LEFT)
        
        self.paper_button = tk.Button(self.root, image=self.paper_img, command=lambda: self.play_round("paper"))
        self.paper_button.pack(pady=5, side=tk.LEFT)
        
        self.scissors_button = tk.Button(self.root, image=self.scissors_img, command=lambda: self.play_round("scissors"))
        self.scissors_button.pack(pady=5, side=tk.LEFT)

    def resize_image(self, image, size=(100, 100)):
        return image.resize(size, Image.Resampling.LANCZOS)

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1

    def play_round(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        
        self.update_score(result)
        
        self.user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
        self.result_label.config(text=result)
        self.score_label.config(text=f"Scores: You - {self.user_score} | Computer - {self.computer_score}")

root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
