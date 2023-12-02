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
        self.max_xcor = 420
        self.min_xcor = -420
        self.max_ycor = 210
        self.min_ycor = 100
        self.all_bricks = []

    def generate_bricks(self):  # generate the bricks
        columns = 18  # this is constant with current settings
        rows = 7
        for _ in range(0, columns * rows):
            new_brick = Brick()
            new_brick.hideturtle()
            self.all_bricks.append(new_brick)
        # print('Bricks made')
        # print(len(self.all_bricks))
        self.display_bricks()
        self.bricks_active = True

    def display_bricks(self):
        # displaying the bricks on screen
        x_cor = -435
        y_cor = 209
        random_xcor = [-450, - 435]

        for block in self.all_bricks:
            block.goto(x_cor, y_cor)
            block.showturtle()
            x_cor += 52
            if x_cor > 450:
                y_cor -= 30
                x_cor = random.choice(random_xcor)
