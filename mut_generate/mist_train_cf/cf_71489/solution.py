"""
QUESTION:
Write a function `isValid(s)` that takes a string `s` as input and returns a boolean value indicating whether the string is valid according to the following rules: 

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. The string may contain nested structures, i.e., brackets within brackets.
4. The string may contain additional alphanumeric characters, which do not affect the validity of the string.

The string `s` is guaranteed to contain only the characters `(`, `)`, `{`, `}`, `[`, `]`, and any number of additional alphanumeric characters. The length of `s` is between 1 and 10^4.
"""

def isValid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}  

    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in bracket_map:
            if not stack or bracket_map[char] != stack.pop():
                return False
    return stack == []