
from turtle import Turtle,Screen
import  random

screen = Screen()
screen.colormode(255)
t = Turtle()
t.speed("fastest") # Set the turtle speed to the fastest for a smoother animation
t.hideturtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r,g,b)
    return color

t.pencolor(random_color())

t.pensize(15)


# Number of steps in the random walk
num_steps = 500
directions = [0,90,180,270]


def random_walk(steps, step_length=30):

    for _ in range(steps):

        angle = random.choice(directions)

        t.setheading(angle)
        t.forward(step_length)
        t.pencolor(random_color())

random_walk(num_steps)



screen.title("Random Walk with Turtle")
screen.setup(width=800,height=600)
screen.exitonclick()