"""
QUESTION:
Create the function `median(l: list, cmp_func: callable)` that takes a list `l` containing integers, nested lists, and tuples, as well as a custom comparison function `cmp_func`. The function should return the median of the elements in `l` without using list sorting or built-in features for finding the median. The comparison function `cmp_func` should be used for comparing elements. The function should handle duplicates, tuples with even and odd number compositions, and calculate the median accordingly.
"""

def median(l, cmp_func):
    """
    Returns the median of nested list and tuple elements in 'l' avoiding sorting or inbuilt functions.
    Handles duplicates, tuples characterized by even and uneven number, employs cmp_func for comparison.
    """
    def flatten(lst):
        """Flattens a nested list/tuple"""
        flat_list = []
        for val in lst:
            if isinstance(val, (list, tuple)):
                flat_list.extend(flatten(val))
            else:
                flat_list.append(val)
        return flat_list

    flat_list = flatten(l)
    length = len(flat_list)

    # Implement quickselect to find the median without sorting the entire list
    def quickselect(lst, k):
        if len(lst) == 1:
            return lst[0]
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if cmp_func(x, pivot) < 0]
        middle = [x for x in lst if cmp_func(x, pivot) == 0]
        right = [x for x in lst if cmp_func(x, pivot) > 0]
        if k < len(left):
            return quickselect(left, k)
        elif k < len(left) + len(middle):
            return middle[0]
        else:
            return quickselect(right, k - len(left) - len(middle))

    # Find median
    if length % 2 == 0:
        median1 = quickselect(flat_list, length // 2 - 1)
        median2 = quickselect(flat_list, length // 2)
        median = (cmp_func(median1, 0) + cmp_func(median2, 0)) / 2
    else:
        median = cmp_func(quickselect(flat_list, length // 2), 0)

    return median