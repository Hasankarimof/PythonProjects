from Pomodoro_Timer.main import canvas

THEME_COLOR = "#375362"

from tkinter import *

class QuizInterface:


    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        # self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        # self.word_text = canvas.create_text(100,100, text="Test",font=("Arial",20,"italic"))
        # self.canvas.grid(row=0,column=0)

        self.window.mainloop()