from turtle import Turtle

POSITION = (0, -260)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('black')
        self.goto(POSITION)
        self.speed('slowest')
        self.showturtle()
        self.add_xcor = 10
        self.add_ycor = 10

    def move(self):
        x_position = self.xcor() + self.add_xcor
        y_position = self.ycor() + self.add_ycor
        self.goto(x_position, y_position)

    def bounce_y(self):
        self.add_ycor *= -1

    def bounce_x(self):
        self.add_xcor *= -1

    def reset_(self):
        self.hideturtle()
        self.goto(POSITION)
        self.showturtle()
        self.bounce_y()
