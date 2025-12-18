"""
QUESTION:
Write a function `is_balanced(s)` that checks if a given string `s` has balanced pairs of round, square, and curly braces. The function should return `True` if the string has balanced parentheses and `False` otherwise.
"""

def is_balanced(s):
    stack = []
    balanced_brackets = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in balanced_brackets:
            stack.append(char)
        elif len(stack) == 0 or balanced_brackets[stack.pop()] != char:
            return False

    return len(stack) == 0