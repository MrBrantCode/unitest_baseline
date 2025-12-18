"""
QUESTION:
Create a function called `count_uppercase_letters` that takes a string as input and returns the number of uppercase letters in the string. The function should not use any built-in string methods or functions that directly check for uppercase letters.
"""

def count_uppercase_letters(string):
    count = 0
    for char in string:
        # Check if the character's ASCII value is within the range of uppercase letters
        if ord(char) >= 65 and ord(char) <= 90:
            count += 1
    return count