"""
QUESTION:
Write a function called "correctBracketing" that takes a string of "(" and ")" characters as input. The function should return True if each opening parenthesis is correctly matched with a corresponding closing parenthesis and False otherwise. The function should return False for an empty string or if there are unmatched opening or closing parentheses.
"""

def correctBracketing(s):
    open_brackets = 0
    for char in s:
        if char == "(":
            open_brackets += 1
        elif char == ")":
            if open_brackets == 0:
                return False
            open_brackets -= 1
    return open_brackets == 0