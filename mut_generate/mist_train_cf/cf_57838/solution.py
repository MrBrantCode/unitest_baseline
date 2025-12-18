"""
QUESTION:
Implement a function named `median` that calculates the median of a list of numbers without sorting the list or using built-in sorting or median functions. The function should handle lists with even and odd number of elements, as well as lists with duplicate elements. The function should also accept a custom comparison function `cmp_func` that is used to compare elements in the list.
"""

def median(l: list, cmp_func: callable):
    """Return median of elements in the list l without sorting it or using built-in functions.
    Handles tuples with even and odd number of elements, duplicates, and uses cmp_func for comparisons.
    """
    # Calculate the length of the list
    n = len(l)

    # Find the mid index
    if n % 2 == 0:
        mid1 = n // 2 - 1
        mid2 = n // 2
    else:
        mid = n // 2

    # Iterate list and find the median
    for idx, val in enumerate(l):
        count = 0
        if n % 2 == 0:
            for i in l[:idx] + l[idx+1:]:
                count += cmp_func(val, i) >= 0  # Count elements smaller than or equal
            if count == mid1 or count == mid2:
                if count == mid1:  # Return mean of mid1 and mid2
                    mid1_val = val
                else:
                    return (mid1_val + val) / 2
        else:
            for i in l[:idx] + l[idx+1:]:
                count += cmp_func(val, i) >= 0  # Count elements smaller than or equal
            if count == mid:
                return val