"""
QUESTION:
Write a function named `median` that takes a list of numbers as input and returns the median of the numbers in the list without sorting the list. The function should handle both lists with an even and an odd number of elements. The median for a list with an odd number of elements is the middle number, and the median for a list with an even number of elements is the average of the two middle numbers.
"""

def median(l: list):
    n = len(l)

    def _quickselect(lst, k, pivot_fn):
        if len(lst) == 1:
            return lst[0]

        pivot = pivot_fn(lst)

        lows = [el for el in lst if el < pivot]
        highs = [el for el in lst if el > pivot]
        pivots = [el for el in lst if el == pivot]

        if k < len(lows):
            return _quickselect(lows, k, pivot_fn)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return _quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

    if n % 2 == 1:
        return _quickselect(l, n // 2, pivot_fn=lambda x: x[len(x) // 2])
    else:
        left = _quickselect(l, n // 2 - 1, pivot_fn=lambda x: x[len(x) // 2])
        right = _quickselect(l, n // 2, pivot_fn=lambda x: x[len(x) // 2])

        return (left + right) / 2