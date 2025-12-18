"""
QUESTION:
Create a function `sort_lowercase_letters` that takes a string as input and returns a new string containing the same lowercase letters, in ascending order of their ASCII values, ignoring any non-lowercase characters.
"""

def sort_lowercase_letters(string):
    lowercase_letters = [char for char in string if char.islower()]
    sorted_letters = sorted(lowercase_letters, key=lambda x: ord(x))
    return ''.join(sorted_letters)