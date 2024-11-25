from turtle import Turtle

UP = 90 # Direction for upward movement
DOWN = 270 # Direction for downward movement


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.hideturtle()
        self.goto(x_pos,y_pos)
        self.showturtle()


    def move_up(self):
        """Move the paddle up by 20 pixels."""
        if self.ycor() < 220:
            self.goto(self.xcor(), self.ycor() + 20)


    def move_down(self):
        """Move the paddle down by 20 pixels. """
        if self.ycor() > -220:
            self.goto(self.xcor(), self.ycor() - 20)
