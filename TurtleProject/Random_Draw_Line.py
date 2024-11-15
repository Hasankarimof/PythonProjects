from turtle import Turtle, Screen
import random
t = Turtle()
timmy_turtle_shape = t.shape("classic")


colours = ["MediumBlue","Bisque","BlueViolet","Lime","LimeGreen",
           "PaleGreen","PaleTurquoise","Teal","Orange","Cornsilk"]



def position_of_draw():
    t.penup()
    t.goto(0,0)
    t.setheading(360)
    t.pendown()


def draw_polygon(sides, length,color):
    angle = 360 / sides # Calculate the angle
    for _ in range(sides):
        t.forward(length)
        t.right(angle)
        t.color(color)

# Set the side length
side_length = 100

position_of_draw()

# Triangle
draw_polygon(3, side_length,random.choice(colours))

# Square
draw_polygon(4, side_length,random.choice(colours))

# Pentagon
draw_polygon(5, side_length,random.choice(colours))

# Hexagon
draw_polygon(6, side_length,random.choice(colours))

# Heptagon
draw_polygon(7, side_length,random.choice(colours))

# Octagon
draw_polygon(8, side_length,random.choice(colours))

# Nonagon
draw_polygon(9, side_length,random.choice(colours))

# Decagon
draw_polygon(10, side_length,random.choice(colours))




screen = Screen()
# screen.mainloop()
screen.exitonclick()