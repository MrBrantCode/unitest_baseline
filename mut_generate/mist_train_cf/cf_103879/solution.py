"""
QUESTION:
Create a function `remove_white_spaces(text)` that takes a string `text` as input, removes all white spaces while preserving the order of characters, and returns the resulting string. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def remove_white_spaces(text):
    result = ""
    for char in text:
        if char != " ":
            result += char
    return result