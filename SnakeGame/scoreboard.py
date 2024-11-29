from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """Clear the previous score and display the updated score."""
        self.clear()
        self.write(f"Score {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        """Increase the score and refresh the display."""
        self.score +=1
        self.update_score()

    # def game_over(self):
    #     """Display a Game Over message."""
    #     self.goto(0,0)
    #     self.write("Game Over!",align="center",font=("Arial",24,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_score()

    def read_high_score(self):
        """Read the high score from data.txt."""
        try:
            with open(r"C:\Users\Khasan\PycharmProjects\PythonProjects\SnakeGame\data.txt", mode="r") as file:
                return int(file.read())
        except FileNotFoundError:
        # If the file doesn't exist, assume the high score is 0
            return 0

    def save_high_score(self):
        """Save the high score to data.txt."""
        with open(r"C:\Users\Khasan\PycharmProjects\PythonProjects\SnakeGame\data.txt",mode="w") as file:
            file.write(str(self.high_score))