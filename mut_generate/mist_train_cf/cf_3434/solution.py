"""
QUESTION:
Write a function `check_parentheses` that takes a string of parentheses as input and returns `True` if the parentheses are balanced and `False` otherwise. The input string will only consist of '(' and ')' characters and its length will be at most 10^6. The solution should have a time complexity of O(n), where n is the length of the input string.
"""

def check_parentheses(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0