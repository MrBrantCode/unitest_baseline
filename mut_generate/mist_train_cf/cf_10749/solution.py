"""
QUESTION:
Create a function `repeat_characters` that takes a string as an argument and returns an updated string. In the updated string, each non-digit character should be repeated twice, and each digit character should be repeated three times.
"""

def repeat_characters(s):
    result = ''
    for char in s:
        if char.isdigit():
            result += char * 3
        else:
            result += char * 2
    return result