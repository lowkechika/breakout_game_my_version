import os.path
from turtle import Turtle, TK
import turtle


class HighScore(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.high_score = 0
        self.current_score = 0
        self.goto(0, 240)
        self.search_highscore()
        self.update_scoreboard()

    def save_highscore(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open('highscore.txt', 'w') as file:
                file.write(f'{self.high_score}')

    def score_increment(self):
        self.current_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.current_score} High Score: {self.high_score}',
                   align="center",
                   font=("Comic Sans MS", 20, "normal"))

    def search_highscore(self):
        if os.path.isfile('highscore.txt'):
            with open('highscore.txt', 'r') as file:
                try:
                    high_score = int(file.readline())
                    self.high_score = high_score
                except ValueError:
                    TK.messagebox.showinfo(title="Oooops!",
                                           message="This isn't right! Somebody messed with the save file! We've fixed "
                                                   "it for you ;)")
                    with open('highscore.txt', 'w') as new_file:
                        new_file.write(f'{self.high_score}')


