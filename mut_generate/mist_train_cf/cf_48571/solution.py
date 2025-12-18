"""
QUESTION:
Write a function `sort_even_indices` that takes a list `l` and returns a new list where the values at even indexes are sorted in ascending order, while the values at odd indexes remain the same as in the original list. The function must have a time complexity of O(n log n) for the sort operation.
"""

def sort_even_indices(l: list):
    # Extract the numbers at even indices from the list
    nums_at_even_indices = [l[i] for i in range(0, len(l), 2)]

    # Sort the extracted numbers
    nums_at_even_indices.sort()

    # Generate the result by merging sorted numbers and numbers at odd indices
    res = [None] * len(l)
    res[::2] = nums_at_even_indices
    res[1::2] = l[1::2]

    return res