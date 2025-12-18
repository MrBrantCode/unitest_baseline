"""
QUESTION:
Write a function `isValidParenthesesOrder` that determines if the order of parentheses in a given string is valid. The function takes a string `s` containing a series of parentheses, brackets, and curly braces as input and returns `True` if every opening parenthesis has a corresponding closing parenthesis in the correct order, and `False` otherwise.
"""

def isValidParenthesesOrder(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
    
    return not stack