"""
QUESTION:
Write a function `isValidParentheses` that takes a string `s` as input and returns `true` if the string is valid, where valid means that the parentheses, brackets, and curly braces are properly nested and closed. The function should return `false` otherwise. The input string only contains parentheses, brackets, and curly braces.
"""

def isValidParentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack