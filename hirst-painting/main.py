import colorgram
import random
from turtle import  Turtle,Screen

screen = Screen()
screen.colormode(255)
screen.setup(width=600,height=600)
screen.title("Spirograph Dot Pattern")

t = Turtle()
t.speed("fastest")
t.hideturtle()
t.penup()

color_list = [(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9),
              (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71),
              (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251),
              (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111),
              (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9),
              (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

t.goto(-225,-225)


def draw_dot():
    color = random.choice(color_list)
    t.dot(20,color)

t.setheading(50)
t.forward(50)
t.setheading(0)


number_of_dots = 100
for row in range(10):
    for col in range(10):
        draw_dot()
        t.forward(50)

    t.backward(500)  # Move back to the beginning of the row
    t.left(90)
    t.forward(50)  # Move down to the next row
    t.right(90)

screen.exitonclick()