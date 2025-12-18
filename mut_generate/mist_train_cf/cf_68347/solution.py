"""
QUESTION:
Implement a function "median" that calculates the median of elements in a list without using built-in sorting functions or sorting the list. The function should handle lists containing integers and floats, including negative numbers, and use a provided comparison function for comparisons. The function should be able to handle tuples with even and odd number of elements and duplicates. The function should take two parameters: a list of numbers and a comparison function.
"""

def partition(l, lo, hi, cmp_func):
    pivot = l[hi]
    i = lo - 1
    for j in range(lo, hi):
        if cmp_func(l[j], pivot) <= 0:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[hi] = l[hi], l[i+1]
    return i + 1

def select_nth(l, n, cmp_func, lo=None, hi=None):
    if lo is None: lo = 0
    if hi is None: hi = len(l) - 1
    pivot_index = partition(l, lo, hi, cmp_func)
    if n == pivot_index:
        return l[n]
    elif n < pivot_index:
        return select_nth(l, n, cmp_func, lo, pivot_index - 1)
    else:
        return select_nth(l, n, cmp_func, pivot_index + 1, hi)

def median(l, cmp_func):
    if not l: 
        return None
    n = len(l)
    if n % 2 == 1:
        return select_nth(l, n // 2, cmp_func)
    else:
        return (select_nth(l, n // 2 - 1, cmp_func) + select_nth(l, n // 2, cmp_func)) / 2.0