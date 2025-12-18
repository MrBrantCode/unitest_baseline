"""
QUESTION:
Write a function called `repeat_characters` that takes a string as input and returns a string where each character from the input string is repeated three times with a space in between each repetition. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def repeat_characters(string):
    result = ''
    for char in string:
        result += char + ' ' + char + ' ' + char + ' '
    return result.strip()