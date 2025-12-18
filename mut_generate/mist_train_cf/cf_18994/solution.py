"""
QUESTION:
Write a function `find_median(x)` that calculates the median of a list of integers `x`. The input list `x` has at least one element. The function should handle both even and odd number of elements in the list and have a time complexity of O(n log n).
"""

def find_median(x):
    x.sort()  # Sort the list in ascending order

    n = len(x)
    if n % 2 == 0:
        # If the number of elements is even
        mid1 = x[n//2]
        mid2 = x[n//2 - 1]
        median = (mid1 + mid2) / 2
    else:
        # If the number of elements is odd
        median = x[n//2]

    return median