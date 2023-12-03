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
        score.attempts -= 1
    elif ball.distance(paddle) < 30:
        ball.bounce_y()
    for block in brick.all_bricks[0: 108]:
        if ball.distance(block) < 25:
            try:
                block.hideturtle()
                brick.all_bricks.remove(block)
                score.score_increment()  # add 1 to current score
                ball.bounce_y()
                score.save_highscore()
            except ValueError:
                pass


def clear_bricks():
    try:
        for block in brick.all_bricks:
            block.clear()
    except ValueError:
        pass


def play_game():
    window.tracer(0)
    score.player_achievement()
    if score.attempts > 0:
        brick.generate_bricks()

        detect_collision()
        ball.move()
        window.update()

    elif score.attempts == 0:
        if score.player_choice:
            score.attempts = 3
            clear_bricks()
            brick.reset_()
            brick.bricks_active = False
            score.player_choice = None
        else:
            if score.player_choice is not None:
                window.bye()
    else:
        pass
    window.ontimer(play_game, 50)


play_game()

window.mainloop()
