"""
QUESTION:
Create a function called `is_brackets_matched` that takes a string of characters as input. The string may contain different types of brackets ((), [], {}) and other characters. The function should return True if the brackets in the string are correctly nested and closed in the correct order, and False otherwise.
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