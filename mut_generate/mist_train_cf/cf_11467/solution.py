"""
QUESTION:
Write a function `is_brackets_matched` that takes a string as input and returns `True` if the brackets in the string are correctly matched and `False` otherwise. The string may contain other characters besides brackets. The function should handle different types of brackets such as `{}`, `[]`, and `()`, which must be correctly nested and closed in the correct order.
"""

def is_brackets_matched(string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0 or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0