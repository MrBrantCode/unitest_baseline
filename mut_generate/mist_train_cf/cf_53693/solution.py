"""
QUESTION:
Create a function named `is_nested` that takes a string of only square brackets and parentheses as input. The function should return `True` if and only if there is a valid subsequence of brackets where at least one bracket in the subsequence is nested and the open-close brackets are balanced.
"""

def is_nested(string):
    stack = []
    nested = False
    for c in string:
        if c in '[({':
            if stack:
                nested = True
            stack.append(c)
        else:
            if not stack:
                return False
            if c == ']' and stack[-1] == '[' or c == ')' and stack[-1] == '(' or c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return len(stack) == 0 and nested