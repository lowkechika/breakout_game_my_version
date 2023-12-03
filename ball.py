from turtle import Turtle

POSITION = (0, -260)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(POSITION)
        self.add_xcor = 10
        self.add_ycor = 10
        self.ball_active = False

    def move(self):
        self.speed('slowest')
        x_position = self.xcor() + self.add_xcor
        y_position = self.ycor() + self.add_ycor
        self.goto(x_position, y_position)

    def bounce_y(self):
        self.speed('slowest')
        self.add_ycor *= -1

    def bounce_x(self):
        self.speed('slowest')
        self.add_xcor *= -1

    def reset_(self):
        self.speed('slowest')
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.showturtle()
        self.bounce_y()
