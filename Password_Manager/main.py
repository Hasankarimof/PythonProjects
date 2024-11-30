from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

from matplotlib.pyplot import title

FILE_PATH = r"C:\Users\Khasan\PycharmProjects\PythonProjects\Password_Manager\data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(symbols) for _ in range(nr_symbols)] + \
                    [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END) # Clear the existing content
    password_entry.insert(0, password) # Insert the new password
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    # Get the values from the entry widgets
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not password:
        # Show an error message if either field is empty
        messagebox.showerror("Oops","Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                        f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:

            try:
                # Try reading the existing data file
                with open(FILE_PATH, "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                # If the file doesn't exist, create it with the new data
                with open(FILE_PATH, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # If the file exists, update the old data with the new data
                data.update(new_data)
                # Save the updated data back to the file
                with open(FILE_PATH, "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # Clear input fields (assuming you're using a GUI with `Entry` widgets)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()

    try:
        with open(FILE_PATH,"r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for the website '{website}' exist.")


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage

# Initialize the main window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

# Create a canvas for the lock icon
canvas = Canvas(window, height=200, width=200)
logo_img = PhotoImage(file="C:/Users/Khasan/PycharmProjects/PythonProjects/Password_Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels and Entry widgets for the user input
website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(window, width=21)
website_entry.grid(row=1, column=1, sticky="ew")
search_button = Button(window, text="Search",width=15,command=find_password)
search_button.grid(row=1, column=2)
website_label.focus()

email_label = Label(window, text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0,"example@gmail.com")

password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1, sticky="ew")

# Button to generate a password
generate_password_button = Button(window, text="Generate Password",command=password)
generate_password_button.grid(row=3, column=2)

# Button to add the password
add_button = Button(window, text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()

