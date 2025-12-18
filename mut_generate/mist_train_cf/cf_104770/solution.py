"""
QUESTION:
Create a function called remove_last_two_chars that takes a string as input and returns the string with its last two characters removed, without using any built-in string methods like slicing with negative indices. The function should work with strings of any length, including those with less than two characters.
"""

def remove_last_two_chars(input_string):
    return input_string[:len(input_string)-2]