from turtle import Turtle

POSITION = (0, -280)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('green')
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(POSITION)
        self.showturtle()

    def move_right(self):
        x_position = self.xcor() + 50
        self.goto(x_position, self.ycor())

    def move_left(self):
        x_position = self.xcor() - 50
        self.goto(x_position, self.ycor())
