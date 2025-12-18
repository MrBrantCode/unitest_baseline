"""
QUESTION:
Create a function called `remove_superfluous_whitespace` that takes a string as input and returns a new string with superfluous whitespace characters removed, while maintaining the integrity of the remaining characters. The function should collapse multiple consecutive whitespace characters into a single space.
"""

def remove_superfluous_whitespace(input_string):
    return ' '.join(input_string.split())