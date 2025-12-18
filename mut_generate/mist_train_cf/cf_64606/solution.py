"""
QUESTION:
Given a string `s` composed of the letters 'a', 'b', and 'c' with a length between 1 and 2 * 10^4, write a function `isValid(s)` that returns `True` if `s` can be formed by repeatedly inserting the string "abc" at any position in an initially empty string, and `False` otherwise.
"""

def entance(s):
    stack = []
    for c in s:
        if c == 'c':
            if len(stack) < 2 or stack[-1] != 'b' or stack[-2] != 'a':
                return False
            stack.pop()
            stack.pop()
        else:
            stack.append(c)
    return not stack