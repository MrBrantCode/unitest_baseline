"""
QUESTION:
Implement a function called `is_balanced` that checks if the parentheses, brackets, and curly braces in a given string are balanced. The function should handle nested cases and ignore other characters in the string. It should return `True` if the parentheses, brackets, and curly braces are balanced and `False` otherwise.
"""

def is_balanced(string):
    stack = []
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    matching = {'(': ')', '{': '}', '[': ']'}
    
    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            top = stack.pop()
            if char != matching[top]:
                return False
    
    return len(stack) == 0