"""
QUESTION:
Write a function `remove_consecutive_duplicates` that takes a string as input and returns the string after removing all consecutive duplicates. The function should keep only the first occurrence of consecutive characters.
"""

def remove_consecutive_duplicates(input_string):
    final_string = ""
    previous_character = ""

    for character in input_string:
        if character != previous_character:
            final_string += character
            previous_character = character

    return final_string