from tkinter import *
import pandas as pd
import random
import os

# -------------------------CONSTANTS----------------------#

# Colors and paths for images
BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_IMG = r"C:\Users\Khasan\PycharmProjects\PythonProjects\Flash_Card_Capstone_Pr\images\card_front.png"
CARD_BACK_IMG = r"C:\Users\Khasan\PycharmProjects\PythonProjects\Flash_Card_Capstone_Pr\images\card_back.png"
RIGHT_IMG = r"C:\Users\Khasan\PycharmProjects\PythonProjects\Flash_Card_Capstone_Pr\images\right.png"
WRONG_IMG = r"C:\Users\Khasan\PycharmProjects\PythonProjects\Flash_Card_Capstone_Pr\images\wrong.png"

# Globals for the current word and flip timer
current_word = {}
flip_timer = None

# -------------------------READING DATA ----------------------#

# Try to read the data for words to learn or fall back to the original list
try:
    # Check if the file "words_to_learn.csv" exists
    if os.path.exists("data/words_to_learn.csv"):
        data = pd.read_csv("data/words_to_learn.csv")  # Load the file
        if data.empty:  # If the file is empty, raise an error
            raise ValueError("words_to_learn.csv is empty.")
    else:
        # If "words_to_learn.csv" does not exist, use "french_words.csv"
        data = pd.read_csv("data/french_words.csv")
except (FileNotFoundError, ValueError, pd.errors.EmptyDataError):
    # Handle cases where "words_to_learn.csv" is missing, empty, or corrupted
    print("Error reading words_to_learn.csv. Using french_words.csv instead.")
    data = pd.read_csv("data/french_words.csv")

# Convert the data into a list of dictionaries for easier access
words_list = data.to_dict(orient="records")

# -------------------------FUNCTIONS----------------------#

def next_word():
    """
    Picks the next random word from the list and updates the flashcard with the French word.
    Resets the timer for flipping the card to show the English translation.
    """
    global current_word, flip_timer
    # Cancel any existing flip timer to avoid overlapping
    if flip_timer:
        window.after_cancel(flip_timer)

    # If there are no words left to learn, display a congratulatory message
    if len(words_list) == 0:
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(card_title, text="Congratulations!", fill="black", font=("Ariel", 40, "italic"))
        canvas.itemconfig(word_text, text="You learned all the words!", fill="black", font=("Ariel", 30, "bold"))
        return

    # Pick a random word and display the French side
    current_word = random.choice(words_list)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black", font=("Ariel", 40, "italic"))
    canvas.itemconfig(word_text, text=current_word["French"], fill="black", font=("Ariel", 60, "bold"))

    # Set a timer to flip the card after 3 seconds
    flip_timer = window.after(3000, flip_card)


def flip_card():
    """
    Flips the card to show the English translation of the current word.
    """
    canvas.itemconfig(canvas_image, image=card_back_img)  # Switch to the back image
    canvas.itemconfig(card_title, text="English", fill="white", font=("Ariel", 40, "italic"))
    canvas.itemconfig(word_text, text=current_word["English"], fill="white", font=("Ariel", 60, "bold"))


def wrong_action():
    """
    Handles the ❌ button click: Does not remove the word and proceeds to the next flashcard.
    """
    next_word()


def correct_button():
    """
    Handles the ✅ button click: Removes the current word from the list and saves the updated list to a file.
    """
    global words_list
    # Remove the current word from the list
    words_list = [word for word in words_list if word != current_word]

    # Save the updated list to "words_to_learn.csv" for future sessions
    pd.DataFrame(words_list).to_csv("data/words_to_learn.csv", index=False)

    # Move to the next flashcard
    next_word()

# -------------------------UI SETUP----------------------#

# Create the main Tkinter window
window = Tk()
window.title("Flashy")  # Set the title of the application
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)  # Add padding and background color

# Create a canvas to display the flashcards
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=CARD_FRONT_IMG)  # Load the front image
card_back_img = PhotoImage(file=CARD_BACK_IMG)  # Load the back image
canvas_image = canvas.create_image(400, 263, image=card_front_img)  # Center the image on the canvas
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))  # Add title text
word_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))  # Add the word text
canvas.grid(row=0, column=0, columnspan=2, pady=(0, 20))  # Place the canvas in the grid

# Load button images
right_img = PhotoImage(file=RIGHT_IMG)  # ✅ button image
wrong_img = PhotoImage(file=WRONG_IMG)  # ❌ button image

# Create the ❌ button
wrong_button = Button(
    image=wrong_img,
    borderwidth=0,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    command=wrong_action  # Call the wrong_action function on click
)
wrong_button.grid(row=1, column=0, padx=10, pady=10)

# Create the ✅ button
right_button = Button(
    image=right_img,
    borderwidth=0,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    command=correct_button  # Call the correct_button function on click
)
right_button.grid(row=1, column=1, padx=10, pady=10)

# Custom Styling for Buttons
wrong_button.config(width=150, height=150)  # Set button size for consistency
right_button.config(width=150, height=150)  # Set button size for consistency


# -------------------------START PROGRAM----------------------#

# Start by displaying the first word
next_word()

# Start the Tkinter main loop to display the UI
window.mainloop()
