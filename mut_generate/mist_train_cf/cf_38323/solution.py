"""
QUESTION:
Write a function called `max_nesting_depth` that takes a string of nested braces `{}` as input and returns the maximum depth of nesting. The input string is guaranteed to be a valid sequence of opening and closing braces, where each opening brace `{` is followed by a corresponding closing brace `}`.
"""

def max_nesting_depth(code_snippet):
    max_depth = 0
    current_depth = 0

    for char in code_snippet:
        if char == '{':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == '}':
            current_depth -= 1

    return max_depth