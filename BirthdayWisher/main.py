##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas as pd
from datetime import datetime

# Read the CSV file
birthdays = pd.read_csv("birthdays.csv")

# Get today's date
today = datetime.now()
today_month = today.month
today_day = today.day

# Check if any birthday matches today
birthday_person = birthdays[(birthdays["month"] == today_month) & (birthdays["day"] == today_day)]

# Print the result (for testing)
if not birthday_person.empty:
    print("Today's birthday:", birthday_person)
else:
    print("No birthdays today.")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
import random

# Pick a random letter template
letter_templates = ["letter_templates\letter_1.txt",
                    "letter_templates\letter_2.txt",
                    "letter_templates\letter_3.txt"]
chosen_template = random.choice(letter_templates)

# Replace [NAME] with the person's name
with open(chosen_template, "r") as file:
    letter_content = file.read()

# Get the person's name from the CSV
person_name = birthday_person.iloc[0]["name"]  # Get the first match
personalized_letter = letter_content.replace("[NAME]", person_name)

# Print the personalized letter (for testing)
print(personalized_letter)

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib

# Email credentials
sender_email = "abdukarimovhasan4@gmail.com"
password = "fhtgspnkmnnozzwb"
recipient_email = birthday_person.iloc[0]["email"]

# Compose the email
subject = "Happy Birthday!"
body = personalized_letter
email_message = f"Subject: {subject}\n\n{body}"

# Connect to the SMTP server and send the email
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()  # Secure the connection
    smtp.login(sender_email, password)  # Login
    smtp.sendmail(sender_email, recipient_email, email_message)

print("Email sent successfully!")




