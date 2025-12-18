"""
QUESTION:
Write a function `is_balanced` that takes a string expression as input and checks if the parentheses, curly brackets, and square brackets in the expression are balanced. The function should return `True` if the brackets are balanced and `False` otherwise.
"""

def is_balanced(expression):
    stack = []
    open_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            last_open_bracket = stack.pop()
            if open_brackets.index(last_open_bracket) != closing_brackets.index(char):
                return False
    return len(stack) == 0