"""
QUESTION:
Write a function `encode_string(string)` that takes a string as input and returns a new string where each character is replaced by its corresponding ASCII code. The ASCII codes should be concatenated without any separator.
"""

def entrance(string):
    result = ""
    for char in string:
        result += str(ord(char))
    return result