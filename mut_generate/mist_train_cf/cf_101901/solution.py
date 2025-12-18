"""
QUESTION:
Create a function `remove_alphabets` that takes an alphanumeric string as input and returns a string containing only the numeric characters from the input string.
"""

def remove_alphabets(s):
    return ''.join(filter(str.isdigit, s))