"""
QUESTION:
Implement a function `isBalanced` that takes a string `s` containing only parentheses, brackets, and braces as input, and returns `True` if every opening parenthesis has a corresponding closing parenthesis and they are properly nested, and `False` otherwise.
"""

def isBalanced(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        else:
            if len(stack) == 0 or stack.pop() != mapping[ch]:
                return False

    return len(stack) == 0