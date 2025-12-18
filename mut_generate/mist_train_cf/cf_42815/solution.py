"""
QUESTION:
Implement the `valid_parentheses` function to check if a given string is a valid parentheses sequence. The function takes a string `s` consisting of only '(' and ')' characters as input and returns `True` if each open parenthesis has a corresponding closing parenthesis and the pairs are properly nested, and `False` otherwise.
"""

def valid_parentheses(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  # Unmatched closing parenthesis
            stack.pop()
    return len(stack) == 0  # True if all parentheses are matched, False otherwise