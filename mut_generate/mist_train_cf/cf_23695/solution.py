"""
QUESTION:
Create a function called `repeat_last_two_char` that takes a string as an argument. The function should return a new string where the last two characters of the input string are repeated. If the input string is less than two characters long, return an empty string.
"""

def repeat_last_two_char(string):
    """Takes a string as an argument and returns a new string with the last two characters repeated."""
    if len(string) < 2:
        return ""
    return string[:-2] + string[-2:] * 2