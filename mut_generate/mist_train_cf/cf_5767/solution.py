"""
QUESTION:
Write a function `check_balanced(expression)` that checks if the parentheses, curly brackets, square brackets, and angle brackets in a given expression are balanced. The function should also check if the angle brackets are properly nested. If the angle brackets are not properly nested, return the position of the first occurrence of the incorrectly nested angle brackets. The function should return `True` if the expression is balanced and `False` otherwise, unless an incorrect angle bracket nesting is found, in which case it should return the position of the error.
"""

def check_balanced(expression):
    """
    Checks if the parentheses, curly brackets, square brackets, and angle brackets in a given expression are balanced.
    Also checks if the angle brackets are properly nested. If the angle brackets are not properly nested, 
    returns the position of the first occurrence of the incorrectly nested angle brackets.

    Args:
        expression (str): The input expression to check.

    Returns:
        bool or int: True if the expression is balanced, False otherwise. If an incorrect angle bracket nesting is found, 
        returns the position of the error.
    """

    stack = []
    angle_brackets_stack = []
    angle_brackets_positions = []

    for i, char in enumerate(expression):
        if char in '([{<':
            stack.append(char)
            if char == '<':
                angle_brackets_stack.append('<')
                angle_brackets_positions.append(i)
        elif char in ')]}>':
            if not stack:
                return False
            top = stack.pop()
            if char == ')':
                if top != '(':
                    return False
            elif char == ']':
                if top != '[':
                    return False
            elif char == '}':
                if top != '{':
                    return False
            elif char == '>':
                if top != '<':
                    return False
                angle_brackets_stack.pop()
                angle_brackets_positions.pop()

    if stack or angle_brackets_stack:
        return False

    if angle_brackets_positions:
        return angle_brackets_positions[0]

    return True