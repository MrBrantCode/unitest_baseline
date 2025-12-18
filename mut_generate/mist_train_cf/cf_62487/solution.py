"""
QUESTION:
Develop a function named `swap_tuple` that takes a nested tuple and a target numerical factor as input, and returns the modified nested tuple. The function should invert the placement of the target factor within the tuple and unify any duplicates into a list at their respective positions. If the target factor appears multiple times, it should be encased as a list for those positions after the first instance. The function should be able to handle nested tuples of arbitrary depth.
"""

def swap_tuple(nested_tuple, target, first_occurrence=True):
    swapped = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            new_element = swap_tuple(element, target, first_occurrence=first_occurrence)
        elif element == target:
            new_element = [target, target] if not first_occurrence else target
            first_occurrence = False
        else:
            new_element = element
        swapped.append(new_element)
    return tuple(swapped)