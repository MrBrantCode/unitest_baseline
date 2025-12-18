"""
QUESTION:
Create a function named `generate_dictionary` that takes two parameters, `list_a` and `list_b`. Both `list_a` and `list_b` must have the same length, and all elements in `list_a` must be unique. The function should return a dictionary where the keys are the elements of `list_a` in ascending order, and the corresponding values are the elements of `list_b` in descending order.
"""

def generate_dictionary(list_a, list_b):
    sorted_list_a = sorted(list_a)
    sorted_list_b = sorted(list_b, reverse=True)
    return dict(zip(sorted_list_a, sorted_list_b))