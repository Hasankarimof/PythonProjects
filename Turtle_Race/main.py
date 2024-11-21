import random
import turtle
from turtle import  Turtle,Screen
from matplotlib.pyplot import title
from numpy.ma.core import shape

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")


# List of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Starting position
start_x = -230
start_y = -100

# Create turtles dynamically
turtles = []  # To keep track of turtle objects
for index, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")  # Create a new turtle
    new_turtle.color(color)  # Assign color from the list
    new_turtle.penup()  # Lift the pen to avoid drawing
    new_turtle.goto(start_x, start_y + index * 30)  # Position each turtle
    turtles.append(new_turtle)  # Store the turtle in the list

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")



        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)








screen.exitonclick()
