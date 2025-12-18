"""
QUESTION:
Write a Python function `parseNestedParens` that calculates the highest level of parentheses nesting for each group in a given string. The string contains different groupings of nested parentheses separated by spaces. The function should take a string as input, where each group is separated by a space, and return a list of integers representing the maximum nesting levels for each group.
"""

def parseNestedParens(paren_string):
    groups = paren_string.split(' ')
    nesting_levels = []

    for group in groups:
        max_depth = 0
        current_depth = 0

        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1

        nesting_levels.append(max_depth)

    return nesting_levels