"""
QUESTION:
Write a function `maxNestingDepth` that takes a string of "done" statements indented with a consistent number of spaces as input and returns the maximum depth of nesting. The function should consider the number of spaces used for indentation before each "done" statement to determine the depth.
"""

def maxNestingDepth(s):
    max_depth = 0
    current_depth = 0
    for char in s:
        if char == ' ':
            current_depth += 1
        else:
            max_depth = max(max_depth, current_depth // 2)
            current_depth = 0
    return max_depth