import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        """Initialize the player at the starting position."""
        self.player = turtle.Turtle()
        self.player.shape("turtle")
        self.player.color("black")
        self.player.penup() # Prevent drawing
        self.player.goto(STARTING_POSITION)
        self.player.left(90)


    def move_up(self):
        """Move the player upward by MOVE_DISTANCE"""
        new_y = self.player.ycor() + MOVE_DISTANCE  # Calculate new Y position
        self.player.goto(self.player.xcor(), new_y)  # Move the turtle

    def distance(self, other):
        """Delegate the distance method to the turtle project."""
        return self.player.distance(other)

    def reset_position(self):
        """Reset the player to the starting position"""
        self.player.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if the player has reached the finish line"""
        return self.player.ycor() >= FINISH_LINE_Y
