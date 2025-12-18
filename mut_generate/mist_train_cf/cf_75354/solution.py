"""
QUESTION:
Write a function called `is_parentheses_balanced` that takes a string `s` as an argument and returns a boolean value indicating whether the parentheses in the string are balanced. The function should consider the following types of parentheses: round brackets "()", square brackets "[]", and curly brackets "{}". It should return `True` if each opening parenthesis has a corresponding closing one and vice versa, and `False` otherwise.
"""

def is_parentheses_balanced(s: str) -> bool:
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        elif char in mapping.values():
            stack.append(char)
    return not stack