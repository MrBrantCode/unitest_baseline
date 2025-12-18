"""
QUESTION:
Write a function `intricate_nested_parentheses` that takes a list of strings consisting only of open and close parentheses. The function should return 'Yes' if a valid sequence of correctly ordered parentheses can be formed by concatenating the strings, and 'No' otherwise.
"""

def intricate_nested_parentheses(lst):
    stack = []
    for string in lst:
        for char in string:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return 'No'
    return 'Yes' if not stack else 'No'