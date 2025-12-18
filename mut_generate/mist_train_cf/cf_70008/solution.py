"""
QUESTION:
Write a function `check_lists(A, B)` that checks if all elements of a potentially nested list `B` are present in a list `A`, where elements in `B` can be nested to any level. The function should return `True` if all elements of the flattened `B` are in `A`, and `False` otherwise. The function should also consider the time and space complexity related to the nesting level in list `B`.
"""

def entrance(A, B):
    """Checks if all items in potentially nested list B are in list A."""
    def flatten(lst):
        flat_lst = []
        for el in lst:
            if isinstance(el, list):
                flat_lst += flatten(el)
            else:
                flat_lst.append(el)
        return flat_lst

    # Flatten B
    flattened_B = flatten(B)
    # Check membership
    return all(item in A for item in flattened_B)