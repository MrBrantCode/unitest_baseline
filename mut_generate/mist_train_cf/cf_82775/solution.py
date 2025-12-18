"""
QUESTION:
Write a function named `count_lines_of_code` that takes a string of Python code as input and returns the number of functional lines of code, ignoring lines containing only comments or whitespace. The function should handle different Python control structures. The input string may contain multiline comments and strings that are not assigned to a variable, which should be treated as lines of generic code.
"""

import ast

def count_lines_of_code(code):
    module = ast.parse(code)
    lines = set()
    for node in ast.walk(module):
        if hasattr(node, "lineno"):
            lines.add(node.lineno)
    return len(lines)