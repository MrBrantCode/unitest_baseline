"""
QUESTION:
Create a function `concatenate_characters` that takes a string as input and returns a new string formed by concatenating the first and last characters of the input string. If the length of the input string is odd, remove the middle character before concatenating.
"""

def concatenate_characters(string):
    if len(string) % 2 == 1:
        middle_index = len(string) // 2
        return string[0] + string[-1] if middle_index == 0 else string[0] + string[-1]
    else:
        return string[0] + string[-1]