"""
QUESTION:
Create a function named `clone_nested_list` that takes two parameters: `old_list` (a nested list containing immutable sub-elements) and `mutation_func` (a function that defines how to mutate the sub-elements). The function should return a new cloned nested list with the same structure as `old_list` but with its sub-elements mutated according to `mutation_func`, without affecting the original `old_list`.
"""

def clone_nested_list(old_list, mutation_func):
    """
    Clone a nested list and apply a mutation function to its elements.

    Args:
    old_list (list): The original nested list to be cloned.
    mutation_func (function): A function that defines how to mutate the sub-elements.

    Returns:
    list: A new cloned nested list with the same structure as old_list but with its sub-elements mutated according to mutation_func.
    """
    return [[mutation_func(item) for item in sublist] for sublist in old_list]