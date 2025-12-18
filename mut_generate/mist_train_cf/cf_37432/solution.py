"""
QUESTION:
Create a function `count_invalid_parenthesis` that takes a string of parentheses as input and returns the minimum number of invalid parentheses that need to be removed to make the sequence valid. A string of parentheses is valid if every opening parenthesis has a corresponding closing parenthesis, and vice versa.
"""

def min_remove_to_make_valid(string):
    stack = []
    invalid_count = 0

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                invalid_count += 1

    invalid_count += len(stack)
    return invalid_count