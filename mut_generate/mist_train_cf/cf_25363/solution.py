"""
QUESTION:
Write a function `is_balanced` that takes a string `input_string` as an argument. The function should check if the parentheses in `input_string` are balanced and return `True` if they are balanced, `False` otherwise. The input string can contain any characters, but only the parentheses '(', ')' will be considered for balance checking.
"""

def is_balanced(input_string):
    stack = []
    for char in input_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0