from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()
        self.level = 1  # Start at level 1
        self.hideturtle()  # Hide the turtle shape
        self.penup()  # Prevent drawing lines
        self.goto(-280, 260)  # Position the scoreboard at the top left corner
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear and write the current level on the screen."""
        self.clear()  # Clear the previous text
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase the level by 1."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display GAME OVER in the center of the screen."""
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align="center", font=FONT)
