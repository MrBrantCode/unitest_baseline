"""
QUESTION:
Write a function named `removeParentheses` that takes a string `s` as input and returns the string with all text within parentheses removed, handling nested parentheses. The function should be efficient for strings up to 10,000 characters long. Note that the function only removes the innermost parentheses when there are nested parentheses, and it expects the parentheses to be correctly paired.
"""

def removeParentheses(s):
    stack = []
    result = ''
    parentheses_to_remove = set()
    
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                parentheses_to_remove.update(range(stack[-1], i+1))
                stack.pop()
    
    for i, ch in enumerate(s):
        if i not in parentheses_to_remove:
            result += ch
    
    return result