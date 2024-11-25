from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Create paddles
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# Create the ball
ball = Ball()

# Create the scoreboard
scoreboard = Scoreboard()

# Key bindings
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with top/bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with the right paddle
    if ball.xcor() > 330 and ball.distance(right_paddle) < 50:
        ball.bounce_x()

    # Detect collision with the left paddle
    if ball.xcor() < -330 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

    # Check for game over
    if scoreboard.left_score == 5:
        scoreboard.game_over("Left Player")
        game_is_on = False

    if scoreboard.right_score == 5:
        scoreboard.game_over("Right Player")
        game_is_on = False

    screen.update()
