"""
QUESTION:
Write a function `isValid(s)` that takes a string `s` of parentheses as input, where `s` can contain the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`. The function should return `True` if the string is valid and `False` otherwise. A string is valid if it satisfies the following conditions:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- The string may contain nested structures, i.e., brackets within brackets, and these nested structures must also follow the above two rules.

The input string `s` is guaranteed to consist only of the specified parentheses characters and its length will be between 1 and 10^4 (inclusive).
"""

def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for c in s:
        if c in bracket_map.values():
            stack.append(c)
        elif c in bracket_map.keys():
            if not stack or bracket_map[c] != stack.pop():
                return False
    return not stack