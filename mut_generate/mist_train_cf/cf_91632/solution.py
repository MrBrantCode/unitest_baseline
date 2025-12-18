"""
QUESTION:
Create a function `is_balanced_parentheses(string)` that checks if a string of parentheses is balanced. The function should return `True` if the string is balanced and `False` otherwise. The function should handle three types of brackets: `()`, `[]`, and `{}`.
"""

def is_balanced_parentheses(string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False
    
    return len(stack) == 0