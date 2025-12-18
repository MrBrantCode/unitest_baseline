"""
QUESTION:
Write a function `convert_string` that takes a string as input and returns a new string with all words separated by a single underscore and all punctuation marks removed. The input string may contain uppercase and lowercase letters, punctuation marks, digits, and special characters. The function should ignore non-alphabet characters, handle multiple consecutive spaces, and remove leading and trailing spaces. The function should have a time complexity of O(n), where n is the length of the input string, and minimize memory usage and string operations.
"""

import string

def convert_string(input_string):
    # Remove leading and trailing spaces
    input_string = input_string.strip()

    # Initialize an empty list to store the modified words
    words = []

    # Initialize a variable to keep track of the current word
    current_word = ""

    # Iterate through each character in the input string
    for char in input_string:
        # If the character is a letter, add it to the current word
        if char.isalpha():
            current_word += char
        # If the character is a space, add the current word to the list
        # if it is not empty, and reset the current word
        elif char == " ":
            if current_word:
                words.append(current_word)
                current_word = ""
        # If the character is a punctuation mark, ignore it
        elif char in string.punctuation:
            continue

    # Add the last word to the list if it is not empty
    if current_word:
        words.append(current_word)

    # Join the words with underscores and return the result
    return "_".join(words)