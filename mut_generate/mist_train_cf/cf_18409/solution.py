"""
QUESTION:
Write a function `calculate_letters` that takes a string as input and returns the total number of letters, uppercase letters, lowercase letters, and non-letter characters (excluding spaces and punctuation marks) in the string.
"""

def calculate_letters(string):
    letters = 0
    uppercase_letters = 0
    lowercase_letters = 0
    non_letters = 0

    for char in string:
        if char.isalpha():
            letters += 1
            if char.isupper():
                uppercase_letters += 1
            else:
                lowercase_letters += 1
        elif char != " " and not char.isalnum() and not char.isspace():
            non_letters += 1

    return letters, uppercase_letters, lowercase_letters, non_letters