from turtle import Turtle
import random

colors = ['red', 'green', 'purple', 'skyblue', 'black']


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks_active = False
        self.shape('square')
        self.color(random.choice(colors))
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.shapesize(stretch_wid=1, stretch_len=1.8)
        self.x_cor = -435
        self.y_cor = 209
        self.all_bricks = []

    def generate_bricks(self):  # generate the bricks
        if not self.bricks_active:
            # print('Generating bricks!')
            columns = 18  # this is constant with current settings
            rows = 6
            for _ in range(0, columns * rows):
                new_brick = Brick()
                new_brick.hideturtle()
                self.all_bricks.append(new_brick)
            self.display_bricks()
            self.bricks_active = True

    def display_bricks(self):
        # displaying the bricks on screen
        random_xcor = [-450, - 435]

        for block in self.all_bricks[0: 108]:
            self.clear()
            block.goto(self.x_cor, self.y_cor)
            block.showturtle()
            self.x_cor += 52
            if self.x_cor > 450:
                self.y_cor -= 30
                self.x_cor = random.choice(random_xcor)

    def reset_(self):
        self.y_cor = 209
        self.x_cor = -435

    def clear_(self):
        try:
            for block in self.all_bricks[0: 108]:
                block.clear()
        except ValueError:
            pass
