"""
QUESTION:
Create a function called `repeat_characters` that takes a string as input, repeats each character in the string three times, and returns the resulting string repeated twice with three spaces in between. The function should handle any input string.
"""

def repeat_characters(s):
    repeated_string = ''.join([char * 3 for char in s])
    return repeated_string + "   " + repeated_string