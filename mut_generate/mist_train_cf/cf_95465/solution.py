"""
QUESTION:
Create a function called `find_median` that takes a list of integers as input and returns the median of the list. The input list will have at least one element and the function should handle both even and odd number of elements. The time complexity of the function should be O(nlogn).
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