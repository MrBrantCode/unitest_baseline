"""
QUESTION:
Create a function named `list_to_dict` that takes two lists, `first_list` and `second_list`, as arguments. The function should return a dictionary where the elements from `second_list` are used as keys, and the corresponding values are lists of indices where each key appears in `first_list`. The function should be able to handle duplicate elements in both lists.
"""

def list_to_dict(first_list, second_list):
    return {x: [i for i, e in enumerate(first_list) if e == x] for x in second_list}