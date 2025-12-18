"""
QUESTION:
Implement a function `check_balanced_parentheses` that takes a string as input and returns `True` if the string has balanced parentheses and `False` otherwise. The string may contain other characters apart from parentheses. The function should consider the following types of parentheses: '(', ')', '{', '}', '[', ']'.
"""

def check_balanced_parentheses(string):
    stack = []
    opening_parentheses = ['(', '{', '[']
    closing_parentheses = [')', '}', ']']
    for char in string:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if opening_parentheses.index(top) != closing_parentheses.index(char):
                return False
    return len(stack) == 0