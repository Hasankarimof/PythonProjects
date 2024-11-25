from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05  # Start with a standard speed


    def move(self):
        """Move the ball by updating its position."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        """Reverse the y direction when hitting the top/bottom walls."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the x direction when hitting a paddle."""
        self.x_move *= -1

    def reset_position(self):
        """Reset the ball to the center and reverse direction."""
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.05  # Reset speed to the original value