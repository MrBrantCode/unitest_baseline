"""
QUESTION:
Write a function `parse_generator_expression(generator_expression)` that takes a string representing a generator expression as input. The string consists of a series of operations, each represented by a class name followed by its arguments in square brackets. The function should return a list of operations in the order they are applied.

The input string may contain nested operations, and each operation may have multiple arguments. The function should correctly handle these cases and return a list of operations as strings, including their arguments and parentheses.
"""

import re

def parse_generator_expression(generator_expression):
    operations = re.findall(r'(\w+\([^)]*\))', generator_expression)
    return operations