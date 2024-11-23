from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """Clear the previous score and display the updated score."""
        self.clear()
        self.write(f"Score {self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        """Increase the score and refresh the display."""
        self.score +=1
        self.update_score()

    def game_over(self):
        """Display a Game Over message."""
        self.goto(0,0)
        self.write("Game Over!",align="center",font=("Arial",24,"normal"))