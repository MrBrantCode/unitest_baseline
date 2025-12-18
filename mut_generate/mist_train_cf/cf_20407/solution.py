"""
QUESTION:
Create a function `check_balanced(expression)` that takes a string `expression` as input and returns a boolean indicating whether the parentheses, curly brackets, square brackets, and angle brackets in the expression are balanced or not. The function should return `True` if the brackets are balanced and `False` otherwise.
"""

def check_balanced(expression):
    stack = []
    opening_brackets = {'(', '{', '[', '<'}
    closing_brackets = {')', '}', ']', '>'}
    bracket_pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            last_opening_bracket = stack.pop()
            if bracket_pairs[last_opening_bracket] != char:
                return False

    return len(stack) == 0