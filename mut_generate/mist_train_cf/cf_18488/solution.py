"""
QUESTION:
Create a function `is_valid_brackets` that takes a string `s` of brackets and possibly other characters as input. The function should return `True` if the brackets in the string are correctly matched and closed in the correct order, and `False` otherwise. The function should handle different types of brackets ({}, [], ()), multiple types of brackets nested within each other, multiple layers of nesting, and additional characters between the brackets.
"""

def is_valid_brackets(s):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    opening_brackets = set(brackets.keys())
    closing_brackets = set(brackets.values())
    
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if char != brackets[stack.pop()]:
                return False
    
    return len(stack) == 0