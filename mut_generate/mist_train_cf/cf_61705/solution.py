"""
QUESTION:
Write a function named `min_difference` that takes an array of integers as input, sorts it in ascending order without using any pre-defined sort function, and returns a tuple containing the minimum difference between two consecutive elements and the total count of pairs with this minimal difference.
"""

def min_difference(arr):
    """
    Sorts the input array in ascending order without using any pre-defined sort function 
    and returns a tuple containing the minimum difference between two consecutive elements 
    and the total count of pairs with this minimal difference.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the minimum difference and the count of pairs with this difference.
    """

    # Sort the array using bubble sort
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    min_diff = float('inf')
    min_pairs = 0

    # Loop through the array to find the minimum difference and number of such pairs
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < min_diff:
            min_diff = diff
            min_pairs = 1
        elif diff == min_diff:
            min_pairs += 1

    return min_diff, min_pairs