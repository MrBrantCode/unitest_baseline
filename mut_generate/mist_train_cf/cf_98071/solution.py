"""
QUESTION:
Implement a function `is_valid_parentheses(s: str) -> bool` that evaluates the authenticity of a given sequence of parentheses. The function should handle different types of brackets including square brackets, curly brackets, and angle brackets in addition to the traditional round brackets, checking for balance, proper positioning, unmatched brackets, overlapping brackets, and improper nesting.
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