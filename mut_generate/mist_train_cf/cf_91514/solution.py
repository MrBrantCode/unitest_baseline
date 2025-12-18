"""
QUESTION:
Create a function called `repeat_characters` that takes a string as an argument and returns an updated string where each character is repeated twice, except for digits which should be repeated three times.
"""

def repeat_characters(string):
    result = ''
    for char in string:
        if char.isdigit():
            result += char * 3
        else:
            result += char * 2
    return result