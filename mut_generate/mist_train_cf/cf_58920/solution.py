"""
QUESTION:
Create a function `isNested` that takes a string of only square brackets as input and returns True if the string contains at least one nested pair of brackets, False otherwise. The string can be empty and can contain any number of opening and closing brackets. The function should check if the brackets are properly nested and if there is at least one pair of nested brackets.
"""

def isNested(s: str) -> bool:
    """
    Checks if a string of square brackets contains at least one nested pair of brackets.

    Args:
    s (str): The input string containing only square brackets.

    Returns:
    bool: True if the string contains at least one nested pair of brackets, False otherwise.
    """
    bracket_stack = []
    for char in s:
        if char == '[':
            bracket_stack.append(char)
        elif char == ']':
            if not bracket_stack:
                return False
            bracket_stack.pop()
    return bracket_stack == [] and '[' + ']' in s