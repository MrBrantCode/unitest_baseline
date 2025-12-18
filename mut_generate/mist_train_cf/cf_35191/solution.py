"""
QUESTION:
Write a function `is_balanced_parentheses(s: str) -> bool` that determines whether the parentheses in a given string `s` are balanced. The string may contain other characters besides parentheses, which should be ignored. The function should return `True` if the parentheses are balanced and `False` otherwise. The input string `s` is of length 1 to 10^5.
"""

def is_balanced_parentheses(s: str) -> bool:
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or bracket_pairs[stack.pop()] != char:
                return False

    return not stack