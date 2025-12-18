"""
QUESTION:
Write a function `is_valid_parentheses(s)` that evaluates the authenticity of a given sequence of parentheses. The function should handle different types of brackets including square brackets, curly brackets, angle brackets, and round brackets, and check for balance, position, and proper nesting. The function should return `True` if the sequence is valid and `False` otherwise. The input `s` is a string containing various types of brackets.
"""

def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "[", ">": "<"}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            return False
    return not stack