"""
QUESTION:
Write a function `isBalancedBraces(code: str) -> bool` that takes a string `code` containing curly braces, spaces, tabs, and C++-style comments, and returns `True` if the curly braces are properly balanced within the code snippet, ignoring characters within the comments denoted by `//` that extend to the end of the line.
"""

def isBalancedBraces(code: str) -> bool:
    stack = []
    in_comment = False

    for char in code:
        if char == '/' and not in_comment and len(stack) > 0 and stack[-1] == '{':
            in_comment = True
        elif char == '\n' and in_comment:
            in_comment = False
        elif not in_comment:
            if char == '{':
                stack.append('{')
            elif char == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop()

    return len(stack) == 0