"""
QUESTION:
Write a function called `count_code_lines` that counts and returns the total number of lines in a given Python function, where each line is counted separately regardless of indentation or nesting.
"""

def count_code_lines(function):
    lines = function.split('\n')
    return len(lines)