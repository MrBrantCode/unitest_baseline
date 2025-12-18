"""
QUESTION:
Write a function `median(l)` that calculates the median of a list of integers, possibly including negative numbers, without sorting the list. The function should handle lists of both even and odd length, and return the median as a float if the list has an even number of elements.
"""

def median_of_list(l):
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

    return quickselect_median(l, pivot_fn=lambda x: x[len(x) // 2])