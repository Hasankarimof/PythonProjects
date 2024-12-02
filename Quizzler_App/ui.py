
THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain
FALSE_IMG = r"C:\Users\Khasan\PycharmProjects\PythonProjects\Quizzler_App\images\false.png"
TRUE_IMG = r"C:\Users\Khasan\PycharmProjects\PythonProjects\Quizzler_App\images\true.png"

class QuizInterface:


    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        # Canvas for question display
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,  # Centered text
            width=280,
            text="Test",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        # Score Label
        self.score_label = Label(text="Score 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        # Load button images
        self.false_img = PhotoImage(file=FALSE_IMG)
        self.true_img = PhotoImage(file=TRUE_IMG)

        # False button
        self.false_button = Button(
            image=self.false_img,
            borderwidth=0,
            highlightthickness=0,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            command=self.false_button
        )
        self.false_button.grid(row=2, column=1)

        # True button
        self.true_button = Button(
            image=self.true_img,
            borderwidth=0,
            highlightthickness=0,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            command=self.true_button
        )
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.canvas.config(bg="yellow")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)


