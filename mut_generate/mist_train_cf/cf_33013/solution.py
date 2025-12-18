"""
QUESTION:
Write a function `isBalancedParentheses` that takes a string `s` containing only "(" and ")" as input and returns `True` if the parentheses are balanced and `False` otherwise. The function should determine whether each opening parenthesis "(" has a corresponding closing parenthesis ")" in the correct order.
"""

def isBalancedParentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  
            stack.pop()
    return len(stack) == 0  