from turtle import Turtle
import random

from TurtleCrossingGame.player import MOVE_DISTANCE

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        """Initialize the car manager."""
        self.all_cars = [] # A list to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE # starting speed of the cars

    def create_car(self):
        """Create a new car at a random y-position."""
        # 1-in-6 chance to generate a car
        if random.randint(1,6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all the cars left."""
        for car in self.all_cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())

    def level_up(self):
        """Increase the speed of the cars."""
        self.car_speed += MOVE_INCREMENT