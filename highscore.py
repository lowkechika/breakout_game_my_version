import os.path
from turtle import Turtle, TK


class HighScore(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.high_score = 0
        self.current_score = 0
        self.goto(0, 240)
        self.search_highscore()
        self.attempts = 5
        self.player_choice = None
        self.player_achievement()

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
                    TK.messagebox.showerror(title="Oooops!",
                                            message="This isn't right! Somebody messed with the save file! We've fixed "
                                                    "it for you ;)")
                    with open('highscore.txt', 'w') as new_file:
                        new_file.write(f'{self.high_score}')

    def player_achievement(self):
        if self.attempts == 0 and self.player_choice is None:
            if self.current_score > self.high_score:
                self.player_choice = TK.messagebox.showinfo(title="Well Done!",
                                                            message=f"Congratulations for beating the High "
                                                                    f"Score!\nYour score is:"
                                                                    f"{self.current_score}You beat the"
                                                                    f"High Score!\nIf you select No, the game will quit")
            else:
                self.player_choice = TK.messagebox.askyesno(title="Game Over!",
                                                            message=f"Thank you for Playing!\nYour score is: "
                                                                    f"{self.current_score}\n"
                                                                    f"Would you like to play again?\nIf you select No, "
                                                                    f"the game will quit")
            self.current_score = 0

