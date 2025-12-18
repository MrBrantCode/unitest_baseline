"""
QUESTION:
Write a function named `median` that takes a list of numbers as input and returns the median of the list without sorting the list or using any built-in functions. The function should handle lists with both even and odd quantities of elements, as well as lists with duplicate elements. The function should also be able to handle tuples as input.
"""

def quickselect_median(l, pivot_fn):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) // 2 - 1, pivot_fn) +
                      quickselect(l, len(l) // 2, pivot_fn))

def quickselect(l, k, pivot_fn):
    if len(l) == 1:
         return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

def pivot_first(l):
    return l[0]

def median(l: list):
    return quickselect_median(l, pivot_first)