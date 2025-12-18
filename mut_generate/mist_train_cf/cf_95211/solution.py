"""
QUESTION:
Create a function `is_valid_brackets` that takes a string of characters as input, which may contain different types of brackets ((), {}, []) and other characters. The function should return True if the brackets are correctly matched and closed in the correct order, and False otherwise. The function should handle cases with multiple types of brackets nested within each other, multiple layers of nesting, and additional characters between the brackets.
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