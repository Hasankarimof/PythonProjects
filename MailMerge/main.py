# Step 1: Read the template letter
with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_template = letter_file.read()  # Read the entire content of the file

# Step 2: Read the names from invited_names.txt
with open("Input/Names/invited_names.txt", "r") as names_file:
    # Use readlines() to get each name as a full line
    names = names_file.readlines()

# Step 3: Create the "ReadyToSend" folder if it doesn't exist
import os
if not os.path.exists("Output/ReadyToSend"):
    os.makedirs("Output/ReadyToSend")

# Step 4: Generate personalized letters
for name in names:
    # Remove extra whitespace, including newline characters
    stripped_name = name.strip()

    # Replace the placeholder [name] with the full name in the template
    personalized_letter = letter_template.replace("[name]", stripped_name)

    # Define the output file path
    output_path = f"Output/ReadyToSend/{stripped_name}_letter.txt"

    # Write the personalized letter to the "ReadyToSend" folder
    with open(output_path, "w") as output_file:
        output_file.write(personalized_letter)

    print(f"Letter for {stripped_name} created at {output_path}")
