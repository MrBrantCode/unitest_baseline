"""
QUESTION:
Implement a function `is_balanced_parentheses` that checks if a given string containing different types of parentheses (round brackets (), square brackets [], and curly brackets {}) is balanced. The function should return `True` if every opening parenthesis has a corresponding closing parenthesis and they are properly nested, and `False` otherwise. The implementation should not use any built-in stack or queue data structures, but rather implement its own stack data structure.
"""

def is_balanced_parentheses(string):
    stack = []

    for c in string:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if len(stack) == 0:
                return False
            opening = stack.pop()
            if (c == ')' and opening != '(') or (c == ']' and opening != '[') or (c == '}' and opening != '{'):
                return False

    return len(stack) == 0