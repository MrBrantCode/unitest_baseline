"""
QUESTION:
Compute the median of an unordered array of numerical elements. The array can contain positive, negative, and decimal values, and may include duplicate numbers. If the array has an even number of elements, return the smaller of the two middle values. If all elements in the array are identical, return the custom error message "All elements are identical, median cannot be computed". The solution should be optimized for larger datasets.
"""

from collections import Counter

def entrance(arr):
    n = len(arr)
    arr.sort()

    # Check if all elements are identical
    if len(Counter(arr)) == 1:
        return "All elements are identical, median cannot be computed"

    # Compute median based on whether n is even or odd
    elif n % 2 != 0:
        return arr[n // 2]
    else:
        return min(arr[n // 2 - 1], arr[n // 2])