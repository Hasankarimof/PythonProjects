import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # turn off the animation
screen.bgcolor("white")
screen.title("Turtle Crossing Game")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()  # Display GAME OVER
            print("Game Over")

    # Detect if the player reaches the finish line
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()  # Update the level

