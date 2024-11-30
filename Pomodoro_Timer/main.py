from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)  # Cancel the current timer
    reps = 0  # Reset reps
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer text
    timer_label.config(text="Timer", fg=GREEN)  # Reset the title
    checkmark_label.config(text="")  # Clear checkmarks

# ---------------------------- TIMER MECHANISM ------------------------------- #
def update_checkmarks():
    global reps
    # Add one checkmark for every two reps
    work_sessions = reps // 2  # Every two reps is one work session
    checkmarks = "✔" * work_sessions
    checkmark_label.config(text=checkmarks)

def start_timer():
    global reps
    reps += 1

    # Calculate the duration for the current session
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine the current session type
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

    update_checkmarks()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02}")  # Update timer text
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

# Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=230, height=240, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file=r"/Pomodoro_Timer\tomato.png")
canvas.create_image(115, 120, image=image)
timer_text = canvas.create_text(115, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_button = Button(
    text="Start",
    font=(FONT_NAME, 12, "bold"),
    highlightbackground=YELLOW,
    highlightthickness=0,
    command=start_timer,
)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(
    text="Reset",
    font=(FONT_NAME, 12, "bold"),
    highlightbackground=YELLOW,
    highlightthickness=0,
    command=reset_timer,
)
reset_button.grid(column=2, row=2)

# Checkmark Label
checkmark_label = Label(text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)

# Footer Label
footer_label = Label(
    text="Stay focused and productive!",
    font=(FONT_NAME, 10, "italic"),
    bg=YELLOW,
    fg=RED,
)
footer_label.grid(column=1, row=4)

window.mainloop()
