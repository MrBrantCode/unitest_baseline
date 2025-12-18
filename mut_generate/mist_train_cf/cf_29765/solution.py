"""
QUESTION:
Given a string `s` consisting of lowercase English letters and curly braces, write a function `isProperlyNested(s: str) -> bool` to determine if the string is properly nested. The function should return `True` if for every opening curly brace there is a corresponding closing curly brace, and they are properly nested within each other, and `False` otherwise.
"""

def entrance(s: str) -> bool:
    stack = []
    opening_braces = {'{', '[', '('}
    closing_braces = {'}', ']', ')'}
    brace_pairs = {'{': '}', '[': ']', '(': ')'}
    
    for char in s:
        if char in opening_braces:
            stack.append(char)
        elif char in closing_braces:
            if not stack or brace_pairs[stack.pop()] != char:
                return False
    
    return not stack