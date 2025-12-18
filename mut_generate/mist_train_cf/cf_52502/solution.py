"""
QUESTION:
Write a function `apply_rule_to_matrix` that takes a 2D list `matrix` and a function `rule` as input, applies the given rule to each element of the matrix independently, and returns a new 2D list with the modified elements. The rule is a mathematical operation that takes one argument.
"""

def apply_rule_to_matrix(matrix, rule):
    """
    Applies a given mathematical rule to each element of a 2D matrix.

    Args:
        matrix (list): A 2D list of elements.
        rule (function): A mathematical operation that takes one argument.

    Returns:
        list: A new 2D list with the modified elements.
    """
    return [[rule(element) for element in row] for row in matrix]