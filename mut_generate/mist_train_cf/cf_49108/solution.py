"""
QUESTION:
Write a function `is_nested` that checks the balance and proper nesting of brackets in a given string. The string contains four types of brackets: round brackets `()`, square brackets `[]`, curly brackets `{}`, and angle brackets `<>`. If the brackets are properly nested and balanced, the function should return `(True, None)`. If the brackets are not properly nested or balanced, the function should return `(False, error_position)`, where `error_position` is a string indicating the position of the error. The function should also check for invalid characters and return their position if found.
"""

def is_nested(string):
    """
    This function checks for the balance and proper nesting of brackets.
    If the brackets are not properly nested or balanced, it returns the position of the error.
    """
    stack = []
    brackets_map = {"(": ")", "[": "]", "{": "}", "<": ">"}

    for index, character in enumerate(string, start=1):
        if character in brackets_map:  # encountered an open bracket
            stack.append(character)
        elif character in brackets_map.values():  # encountered a close bracket
            if not stack or brackets_map[stack.pop()] != character:
                return False, f"Position {index}"
        else:
            return False, f"Position {index} - Invalid character {character}"

    # if the stack is empty then brackets were balanced
    return (not stack, None) if not stack else (False, f"Position {len(string)} - unmatched {stack[-1]}")