import turtle
from ball import Ball
from paddle import Paddle
from bricks import Brick

window = turtle.Screen()
window.setup(width=900, height=600)
window.title('Breakout')

window.listen()

ball = Ball()
ball.speed(0.7)
paddle = Paddle()
brick = Brick()

window.onkey(paddle.move_right, 'Right')
window.onkey(paddle.move_left, 'Left')


def play_game():
    ball.move()
    if ball.xcor() > 430 or ball.xcor() < -430:
        ball.bounce_x()
    elif ball.ycor() > 280:
        ball.bounce_y()
    elif ball.ycor() < -280:
        ball.reset_()
    elif ball.distance(paddle) < 30:
        ball.bounce_y()


game_on = True
while game_on:
    play_game()

window.mainloop()
