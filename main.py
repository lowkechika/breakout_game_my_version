import turtle
from ball import Ball
from paddle import Paddle
from bricks import Brick
from highscore import HighScore


window = turtle.Screen()
window.setup(width=900, height=600)
window.title('Breakout')

ball = Ball()

paddle = Paddle()
brick = Brick()
score = HighScore()

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
                score.score_increment()  # add 1 to current score
                ball.bounce_y()
                score.save_highscore()
            except ValueError:
                pass


def play_game():
    if not brick.bricks_active:
        brick.generate_bricks()
    detect_collision()
    ball.move()
    window.tracer(0)
    window.update()
    window.ontimer(play_game, 1)


play_game()

window.exitonclick()
