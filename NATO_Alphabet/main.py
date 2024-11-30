
import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for _, row in nato_data.iterrows()}

def get_phonetic_code():
    while True:
        try:

            user_word = input("Enter a word: ").upper()
            phonetic_code_words = [nato_dict[letter] for letter in user_word]
            print(phonetic_code_words)
            break # Exit the loop if no exception occurs
        except KeyError:
            # Handle invalid characters
            print("Sorry, only letters in the alphabet are allowed. Please try again.")

get_phonetic_code()