"""
QUESTION:
Implement a function `is_valid_parentheses(s: str) -> bool` that determines if a given string contains a valid set of parentheses. The function should return `True` if the parentheses are properly nested and balanced, and `False` otherwise. The function should handle both open and close parentheses, and any other characters in the input string should be ignored.
"""

def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False

    return not stack