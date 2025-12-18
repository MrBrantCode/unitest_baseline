"""
QUESTION:
Implement a function `median` that calculates the median of a list of numbers without sorting the list or using built-in sorting functions. The function should handle lists containing negative numbers and return `None` if the input list is empty. The list can contain an even or odd number of elements, and the median should be calculated accordingly. The function should return a float value if the list has an even number of elements, and an integer value if the list has an odd number of elements.
"""

def median(l: list):
    """Return median of elements in the list l without sorting it or using built-in functions.
    Handles tuples with negative numbers.
    """
    n = len(l)
    if n == 0:
        return None
    if n == 1:
        return l[0]

    def kth_smallest(arr: list, k: int):
        if k > len(arr):
            return None

        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        if k <= len(left):
            return kth_smallest(left, k)
        elif k <= len(left) + len(equal):
            return pivot
        else:
            return kth_smallest(right, k - len(left) - len(equal))

    if n % 2 == 0:
        median_left = kth_smallest(l, n // 2)
        median_right = kth_smallest(l, n // 2 + 1)
        return (median_left + median_right) / 2
    else:
        return kth_smallest(l, n // 2 + 1)