"""
QUESTION:
Implement the `median` function that calculates the median of a list or a list of tuples. The function should handle lists of both even and odd lengths, deal with duplicates, and not use built-in sorting functions or inherent sorting methods. The function should also use a custom comparison function (`cmp_func`) to compare elements in the list.
"""

def median(numbers, cmp_func, pivot_func):
    if len(numbers) % 2 == 1:
        return quickselect(numbers, len(numbers) // 2, cmp_func, pivot_func)
    else:
        return 0.5 * (quickselect(numbers, len(numbers) // 2 - 1, cmp_func, pivot_func) + quickselect(numbers, len(numbers) // 2, cmp_func, pivot_func))

def quickselect(numbers, k, cmp_func, pivot_func):
    if len(numbers) == 1:
        return numbers[0]

    pivot = pivot_func(numbers)

    lows = [el for el in numbers if cmp_func(el, pivot) < 0]
    highs = [el for el in numbers if cmp_func(el, pivot) > 0]
    pivots = [el for el in numbers if cmp_func(el, pivot) == 0]

    if k < len(lows):
        return quickselect(lows, k, cmp_func, pivot_func)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), cmp_func, pivot_func)

def pivot_first(numbers):
    return numbers[0]

def comparison_func(a, b):
    if isinstance(a, tuple) and isinstance(b, tuple):
        return (a > b) - (a < b)
    else:
        return a - b