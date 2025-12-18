"""
QUESTION:
Write a function named `count_lowercase_letters` that takes a string as input and returns the total number of lowercase letters in the string, ignoring special characters, numbers, and uppercase letters.
"""

def count_lowercase_letters(string):
    lowercase_count = 0
    for char in string:
        if char.islower():
            lowercase_count += 1
    return lowercase_count