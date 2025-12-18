"""
QUESTION:
Create a function `correct_bracketing(brackets)` that checks if a string `brackets` composed of '<, >, {, }, [, ], (, and )' has balanced and properly nested brackets. The function should return `True` if the brackets are balanced and properly nested, and `False` otherwise. The function should only use a stack data structure to track the brackets.
"""

def correct_bracketing(brackets):
    """
    Checks if a string of brackets is balanced and properly nested.

    Args:
    brackets (str): A string composed of '<, >, {, }, [, ], (, and )'.

    Returns:
    bool: True if the brackets are balanced and properly nested, False otherwise.
    """
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '[', '>': '<'}

    for bracket in brackets:
        if bracket in bracket_pairs.values():
            stack.append(bracket)
        elif bracket in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[bracket]:
                return False

    return not stack