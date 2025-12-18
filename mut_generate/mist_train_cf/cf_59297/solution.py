"""
QUESTION:
Create a function called `is_valid_parentheses` that determines whether a given string of parentheses is valid. The function should accept a string `s` as input and return a boolean indicating whether the parentheses are properly paired and nested. The function should only consider the following types of parentheses: round (`()`, square (`[]`), and curly (`{}`).
"""

def is_valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs.keys():
            if not stack or stack.pop() != pairs[c]:
                return False
        else:
            return False

    return not stack