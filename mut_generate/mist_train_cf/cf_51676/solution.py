"""
QUESTION:
Implement a `quickselect_median` function that takes a list `l` and a pivot function `pivot_fn` as parameters, and returns the median of the list using the quickselect algorithm. The `quickselect_median` function should handle both even and odd length lists, and it should use the `quickselect` function to find the median. The `quickselect` function should take a list `l`, an index `k`, and a pivot function `pivot_fn` as parameters, and return the k-th smallest element in the list. The `pivot_fn` function should take a list `l` as a parameter, and return a pivot element from the list. The `pivot_fn` function should also handle lists with fewer than two elements and lists with non-numeric items.
"""

def quickselect_median(l, pivot_fn):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) // 2 - 1, pivot_fn) +
                      quickselect(l, len(l) // 2, pivot_fn))

def quickselect(l, k, pivot_fn):
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


def pivot_fn(l):
    try:
        assert len(l) != 0
        return l[len(l) // 2]
    except AssertionError:
        print("The provided list contains fewer than two elements!")
        return None
    except TypeError:
        print("The provided list contains one or more non-numeric items!")
        return None