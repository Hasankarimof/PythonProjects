from tkinter import *

# Create window
window = Tk()
window.title("Mile to Km Converter")
window.geometry("500x300")  # Set a fixed window size
window.config(bg="#f0f8ff")  # Light blue background for a fresh look

def button_click():
    """Convert miles to kilometers and update the result label."""
    try:
        miles = float(input_box.get())  # Get input from the entry box
        if miles < 0:
            result_label.config(text="Error: Enter positive value!")
            result_label.config(fg="red")  # Error text in red
        else:
            km = miles * 1.609  # Convert miles to kilometers
            result_label.config(text=f"{km:.2f} Km", fg="green")  # Success in green
    except ValueError:
        result_label.config(text="Error: Enter a valid number!", fg="red")  # Handle invalid input

def reset():
    """Reset the input and result fields."""
    input_box.delete(0, END)  # Clear the input field
    result_label.config(text="0 Km", fg="black")  # Reset the result label

# Styling options
label_font = ("Arial", 14, "bold")
entry_font = ("Arial", 14)

# Title Label
title_label = Label(window, text="Miles to Kilometers Converter", font=("Arial", 18, "bold"), bg="#4682B4", fg="white", pady=10)
title_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="EW")

# Label for "is equal to"
equal_label = Label(text="is equal to", font=label_font, bg="#f0f8ff")
equal_label.grid(row=2, column=0, padx=10, pady=10)

# Result Label
result_label = Label(text="0 Km", font=("Arial", 16, "bold"), bg="#f0f8ff")
result_label.grid(row=2, column=1, padx=10, pady=10)

# Label for "Km"
km_label = Label(text="Km", font=label_font, bg="#f0f8ff")
km_label.grid(row=2, column=2, padx=10, pady=10)

# Label for "Miles"
miles_label = Label(text="Miles", font=label_font, bg="#f0f8ff")
miles_label.grid(row=1, column=2, padx=10, pady=10)

# Input Entry for miles
input_box = Entry(width=10, bd=2, font=entry_font, relief="solid", justify="center")
input_box.grid(row=1, column=1, padx=10, pady=10)

# Button to calculate
calculate_button = Button(
    text="Calculate",
    command=button_click,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="raised",
    bd=2
)
calculate_button.grid(row=3, column=1, pady=10)

# Reset button
reset_button = Button(
    text="Reset",
    command=reset,
    bg="#DC143C",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="raised",
    bd=2
)
reset_button.grid(row=4, column=1, pady=10)

# Footer Label
footer_label = Label(
    text="Created with ❤️ using Tkinter",
    font=("Arial", 10, "italic"),
    bg="#f0f8ff",
    fg="#4682B4"
)
footer_label.grid(row=5, column=0, columnspan=3, pady=20)

# Run the main loop
window.mainloop()
