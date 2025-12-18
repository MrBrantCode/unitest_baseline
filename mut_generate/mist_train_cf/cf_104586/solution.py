"""
QUESTION:
Write a function `convert_to_uppercase(input_string)` that takes a string of words as input and returns the string with all words converted to uppercase, separated by a single whitespace, and without leading or trailing whitespaces. The input string only contains alphabetic characters and whitespace.
"""

def convert_to_uppercase(input_string):
    # Split the input string into individual words
    words = input_string.split()

    # Convert each word to uppercase
    uppercase_words = [word.upper() for word in words]

    # Join the uppercase words together with a single whitespace separator
    converted_string = ' '.join(uppercase_words)

    # Remove any leading or trailing whitespaces
    converted_string = converted_string.strip()

    return converted_string