"""
QUESTION:
Design a function `extend_string(s)` that takes a string `s` as input and appends its characters to the end of the string until its length reaches 8. If the input string is empty, the function should return an error message.
"""

def extend_string(s):
    if not s:
        return "Input string cannot be empty."

    while len(s) < 8:
        for char in s:
            if len(s) < 8:
                s += char
            else:
                break
    return s