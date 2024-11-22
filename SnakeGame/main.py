
from turtle import Screen,Turtle
import time
from snake import Snake # Import the Snake class

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create a Snake object
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update() # Manually update the screen
    time.sleep(0.1)  # Add a delay to control the speed of the snake
    snake.move() # Call the move() method of the Snake class


screen.exitonclick()

























screen.exitonclick()