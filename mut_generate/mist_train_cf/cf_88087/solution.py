"""
QUESTION:
Create a function named `is_brackets_matched` that takes a string as input and returns a boolean indicating whether the brackets in the string are correctly matched and closed in the correct order. The function should handle different types of brackets such as {}, [], and (), which may be nested within each other, and may contain additional characters between them.
"""

def is_brackets_matched(string):
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0 or bracket_map[stack[-1]] != char:
                return False
            stack.pop()

    return len(stack) == 0