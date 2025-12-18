"""
QUESTION:
Create a function called `is_uppercase_multiple_of_seven` that takes a character as input and returns a boolean value indicating whether the character is an uppercase letter and its ASCII value is a multiple of 7.
"""

def is_uppercase_multiple_of_seven(char):
    return char.isupper() and ord(char) % 7 == 0