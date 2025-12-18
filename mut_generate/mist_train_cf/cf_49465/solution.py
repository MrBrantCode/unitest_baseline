"""
QUESTION:
Write a function named `process_list` that takes in a list, a list of predicate functions, and a transformation function. The function should filter the list based on all the predicates and apply the transformation function to the filtered results. The function should return the transformed list. The list of predicate functions should be applied using the logical AND operation.
"""

def process_list(lst, predicates, transform):
    """
    Filter the list based on all the predicates and apply the transformation function to the filtered results.

    Args:
        lst (list): Input list
        predicates (list): List of predicate functions
        transform (function): Transformation function

    Returns:
        list: Transformed list
    """
    return list(map(transform, filter(lambda x: all(pred(x) for pred in predicates), lst)))