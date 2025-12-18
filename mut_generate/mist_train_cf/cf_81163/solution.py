"""
QUESTION:
Given a string of parentheses and other characters, write a function `min_remove_to_make_valid` that returns the minimum number of parentheses that need to be removed to make the string valid.
"""

def min_remove_to_make_valid(s):
    stack = []
    to_remove = set()
    
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
    
    to_remove = to_remove.union(set(stack))
    return len(to_remove)