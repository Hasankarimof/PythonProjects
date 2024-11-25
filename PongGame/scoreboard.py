from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        """Display the current scores."""
        self.clear()
        self.goto(-100, 200)  # Position for left player's score
        self.write(self.left_score, align="center", font=("Courier", 24, "normal"))
        self.goto(100, 200)   # Position for right player's score
        self.write(self.right_score, align="center", font=("Courier", 24, "normal"))

    def left_point(self):
        """Increment the left player's score."""
        self.left_score += 1
        self.update_score()

    def right_point(self):
        """Increment the right player's score."""
        self.right_score += 1
        self.update_score()

    def game_over(self, winner):
        """Display the game-over message."""
        self.goto(0, 0)
        self.write(f"Game Over! {winner} Wins!", align="center", font=("Courier", 30, "bold"))
