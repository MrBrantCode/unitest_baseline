"""
QUESTION:
Create a function `is_balanced` that determines whether a given string of parentheses is well-formed (balanced), using a Turing machine-like approach. The function should accept a string of parentheses as input and return `True` if the parentheses are balanced, and `False` otherwise. The Turing machine's tape is represented by the input string, and its behavior is determined by a finite set of states and transition rules.
"""

def is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack