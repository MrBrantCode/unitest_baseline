"""
QUESTION:
Write a function `parse_nested_parens(paren_string)` that takes a string of nested parentheses as input, where parentheses groups are separated by spaces, and returns a list of integers representing the maximum depth of each group. The function should count the maximum depth of nested parentheses for each group, where depth increases when an open parenthesis is encountered and decreases when a close parenthesis is encountered.
"""

def parse_nested_parens(paren_string):
    depths = []
    paren_groups = paren_string.split(" ")

    for paren_group in paren_groups:
        current_depth = 0
        max_depth = 0
        for i in range(len(paren_group)):
            if paren_group[i] == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif paren_group[i] == ')':
                current_depth -= 1

        depths.append(max_depth)

    return depths