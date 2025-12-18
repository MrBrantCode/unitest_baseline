"""
QUESTION:
Write a function `nested_parentheses(s)` that takes a string of space-separated groups of nested parentheses and returns a list of the deepest level of nesting for each group.
"""

def nested_parentheses(s):
    result = []
    for group in s.split(' '):
        count, max_count = 0, 0
        for ch in group:
            if ch == '(':
                count += 1
                max_count = max(max_count, count)
            elif ch == ')':
                count -= 1
        result.append(max_count)
    return result