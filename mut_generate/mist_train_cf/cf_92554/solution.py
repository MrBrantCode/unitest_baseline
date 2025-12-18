"""
QUESTION:
Create a function `count_lowercase_letters` that takes a string as input and returns the total number of lowercase letters in the string, ignoring any non-alphabetic characters.
"""

def count_lowercase_letters(string):
    count = 0
    for ch in string:
        if ch.islower():
            count += 1
    return count