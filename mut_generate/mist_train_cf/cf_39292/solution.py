"""
QUESTION:
Implement a function `is_balanced_braces` that takes a string as input and returns `True` if the string contains a balanced set of curly braces, and `False` otherwise. A balanced set of braces is defined as a string where for every opening curly brace '{', there is a corresponding closing curly brace '}' in the correct order, and the braces are properly nested. The input string may contain other characters in addition to curly braces, but only the curly braces are relevant for determining balance.
"""

def is_balanced_braces(s):
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