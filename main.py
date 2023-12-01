import turtle
from ball import Ball
from paddle import Paddle
from bricks import Brick
import time

window = turtle.Screen()
window.setup(width=900, height=600)
window.title('Breakout')

ball = Ball()
ball.speed(0.05)
paddle = Paddle()
brick = Brick()

# keybindings
window.listen()
window.onkey(paddle.move_right, 'Right')
window.onkey(paddle.move_left, 'Left')


def detect_collision():
    if ball.xcor() > 430 or ball.xcor() < -430:
        ball.bounce_x()
    elif ball.ycor() > 280:
        ball.bounce_y()
    elif ball.ycor() < -280:
        ball.reset_()
    elif ball.distance(paddle) < 30:
        ball.bounce_y()
    for block in brick.all_bricks:
        if ball.distance(block) < 25:
            try:
                block.hideturtle()
                brick.all_bricks.remove(block)
                ball.bounce_y()
            except ValueError:
                pass


brick.generate_bricks()
brick.display_bricks()

game_on = True
while game_on:
    ball.move()
    window.update()
    time.sleep(0.001)
    detect_collision()


window.mainloop()
