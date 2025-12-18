"""
QUESTION:
Implement a function named `median` that takes a list `l` and a comparison function `cmp_func` as parameters. The function should calculate the median of the elements in the list without sorting it or using built-in sorting functions. It should be able to handle lists with even or odd number of elements, duplicates, and use the provided comparison function for comparisons. The function should return the calculated median value.
"""

def median(l: list, cmp_func: callable):
    """Return median of elements in the list l without sorting it or using built-in functions.
    Handles tuples with even and odd number of elements, duplicates, and uses cmp_func for comparisons.
    """
    n = len(l)
    
    # Find the index of the middle elements
    middle_elements_indices = [n // 2] if n % 2 == 1 else [n // 2 - 1, n // 2]

    def find_element_at_index(l, index, cmp_func):
        """Return the element that would be at the given index if the list were sorted using cmp_func."""
        pivot = l[0]

        # Partition the list based on cmp_func
        lower = [x for x in l if cmp_func(x, pivot) < 0]
        upper = [x for x in l if cmp_func(x, pivot) > 0]

        # If the pivot is at the target index, return it
        if index < len(lower):
            return find_element_at_index(lower, index, cmp_func)
        elif index > len(l) - len(upper) - 1:
            return find_element_at_index(upper, index - (len(l) - len(upper)), cmp_func)
        else:
            return pivot

    # Find the middle elements and compute the median
    middle_elements = [find_element_at_index(l, i, cmp_func) for i in middle_elements_indices]
    return sum(middle_elements) / len(middle_elements)