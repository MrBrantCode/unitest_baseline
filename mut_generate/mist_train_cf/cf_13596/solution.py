"""
QUESTION:
Create a function `find_differences(list_a, list_b)` that compares two lists of integers and returns a list of integers that are in `list_a` but not in `list_b` and vice versa. The returned list should maintain the order of elements as in `list_a` for elements present in `list_a` but not in `list_b`, and then append elements present in `list_b` but not in `list_a`.
"""

def find_differences(list_a, list_b):
    differences = [x for x in list_a if x not in list_b]
    differences += [x for x in list_b if x not in list_a]
    return differences