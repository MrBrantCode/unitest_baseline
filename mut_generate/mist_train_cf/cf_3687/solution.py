"""
QUESTION:
Create a function called `is_brackets_matched` that takes a string of characters as input. The function should check if the brackets in the string are correctly matched and closed in the correct order, handling different types of brackets ({}, [], and ()), nested brackets, and additional characters between the brackets. The function should return True if the brackets are correctly matched and False otherwise.
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