"""
QUESTION:
Design a function `minSwapsToSort` that takes an array of integers as input and returns the minimum number of adjacent swaps required to sort the array in ascending order. The function should handle arrays with duplicate elements and have a time complexity of O(n^2) and a space complexity of O(1).
"""

def minSwapsToSort(arr):
    """
    This function calculates the minimum number of adjacent swaps required to sort the array in ascending order.

    Args:
        arr (list): The input list of integers.

    Returns:
        int: The minimum number of adjacent swaps required to sort the array.
    """
    n = len(arr)
    swaps = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return swaps