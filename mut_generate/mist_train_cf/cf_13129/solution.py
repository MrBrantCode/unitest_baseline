"""
QUESTION:
Write a function `is_balanced_parentheses` that checks if a given string has balanced parentheses. The string can contain other characters besides parentheses and can include round brackets (), square brackets [], and curly brackets {}. A string is considered balanced if every opening parenthesis has a corresponding closing parenthesis and they are properly nested. The function should return True if the string is balanced and False otherwise. Do not use any built-in stack or queue data structures; implement your own stack data structure to solve this problem.
"""

def is_balanced_parentheses(string):
    stack = []

    for c in string:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if len(stack) == 0:
                return False
            opening = stack.pop()
            if (c == ')' and opening != '(') or (c == ']' and opening != '[') or (c == '}' and opening != '{'):
                return False

    return len(stack) == 0