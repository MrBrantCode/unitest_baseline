"""
QUESTION:
Write a function `quickselect_median` that takes an array of unique integers `l` and a pivot function `pivot_fn` as input, and returns the median of the array without using any built-in or external libraries. The array is not guaranteed to be sorted. The function should handle both odd and even length arrays.
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