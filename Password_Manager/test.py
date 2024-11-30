# try:
#     # Try to open the file
#     file = open("a_file.txt")
#
#     # Access a value from the dictionary
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
#
# except FileNotFoundError:
#     # If the file is not found, create it and write something
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_message:
#     # Handle a missing key in the dictionary
#     print(f"The key {error_message} does not exist.")
#
# else:
#     # If no exception occurs, read and print the file's content
#     content = file.read()
#     print(content)
#
# finally:
#     # Ensure the file is closed properly
#     file.close()
#     raise TypeError("This is an error that I made up.")
#     print("File was closed.")


# Get user input for height and weight
height = float(input("Height: "))  # Convert the input to a float
weight = int(input("Weight: "))   # Convert the input to an integer

# Print the height and weight to verify input
# print(f"Your height is: {height}")
# print(f"Your weight is: {weight}")


