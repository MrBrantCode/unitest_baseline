"""
QUESTION:
Create a function `remove_items` that takes a list and a set of indices as input, and returns a new list containing only the elements at positions not in the set of indices. The original list should not be modified.
"""

def remove_items(input_list, indices):
    return [elem for i, elem in enumerate(input_list) if i not in indices]