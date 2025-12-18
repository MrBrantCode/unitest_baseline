"""
QUESTION:
Write a function `median` that calculates the median of a list of elements without sorting the list or using built-in sorting functions. The function should handle tuples with both even and odd numbers of elements and duplicate values. It should also accept a custom comparison function `cmp_func` to compare elements. The function should return the median as a float for lists with even numbers of elements.
"""

def median(l: list, cmp_func: callable):
    """
    Calculate the median of a list of elements without sorting the list or using built-in sorting functions.

    Args:
        l (list): The list of elements.
        cmp_func (callable): A custom comparison function to compare elements.

    Returns:
        float: The median of the list as a float for lists with even numbers of elements.
    """
    def select_nth(lst: list, n: int, cmp_func: callable) -> int:
        """
        Helper function to get the nth element of the list according to the order defined by cmp_func
        """
        pivot_fn = lambda array: array[len(array) // 2]
        pivot = pivot_fn(lst)

        lows = [el for el in lst if cmp_func(el, pivot) < 0]
        highs = [el for el in lst if cmp_func(el, pivot) > 0]
        pivots = [el for el in lst if cmp_func(el, pivot) == 0]

        if n < len(lows):
            return select_nth(lows, n, cmp_func)
        elif n < len(lows) + len(pivots):
            return pivots[0]
        else:
            return select_nth(highs, n - len(lows) - len(pivots), cmp_func)

    if len(l) % 2 == 1:
        return select_nth(l, len(l) // 2, cmp_func)
    else:
        return (select_nth(l, len(l) // 2 - 1, cmp_func) + select_nth(l, len(l) // 2, cmp_func)) / 2