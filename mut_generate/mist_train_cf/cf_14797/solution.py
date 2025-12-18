"""
QUESTION:
Create a function named `repeat_characters` that takes a string `string` and an integer `n` as input. The function should return a new string where each character from the original string is repeated `n` times.
"""

def repeat_characters(string, n):
    repeated_string = ""
    for char in string:
        repeated_string += char * n
    return repeated_string