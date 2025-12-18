"""
QUESTION:
Write a function called `check_strings` that takes in a list of strings and returns True if any of the strings (excluding those that start with a lowercase letter) contain the letter 'a'.
"""

def entrance(strings):
    for string in strings:
        # Ignore strings that start with a lowercase letter
        if string[0].islower():
            continue
        # Check if the string contains the letter 'a'
        if 'a' in string:
            return True
    return False