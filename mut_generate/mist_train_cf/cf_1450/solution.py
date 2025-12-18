"""
QUESTION:
Write a function `get_last_character` that takes a string as input, retrieves the last character, and returns it in uppercase. If the input string is empty, return the message "Input string is empty. Please provide a non-empty string."
"""

def get_last_character(string):
    if string:
        last_character = string[-1]
        uppercase_character = last_character.upper()
        return uppercase_character
    else:
        return "Input string is empty. Please provide a non-empty string."