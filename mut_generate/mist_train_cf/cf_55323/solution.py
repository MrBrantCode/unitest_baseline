"""
QUESTION:
Implement the function `correctBracketing` that takes a string `brackets` consisting of "<" and ">" characters and returns a boolean value. The function should return `true` if every opening bracket has a corresponding closing bracket in the correct order, and `false` otherwise. The function should handle multiple outer and nested pairs of brackets.
"""

def correct_bracketing(brackets):
    """
    Checks if every opening bracket has a corresponding closing bracket in the correct order.

    Args:
    brackets (str): A string consisting of "<" and ">" characters.

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append('<')
        elif bracket == '>':
            if not stack:
                return False
            stack.pop()
    return not stack