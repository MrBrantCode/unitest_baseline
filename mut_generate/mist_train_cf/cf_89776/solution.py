"""
QUESTION:
Implement a function `sort_remove_duplicate_sum` that takes an array of integers as input, sorts it in descending order without using any built-in sorting function, removes any duplicate elements in-place, and returns the sum of all positive elements in the array. The input array may contain negative numbers.
"""

def sort_remove_duplicate_sum(arr):
    """
    Sorts the array in descending order, removes any duplicate elements in-place, 
    and returns the sum of all positive elements in the array.

    Args:
    arr (list): The input array of integers.

    Returns:
    int: The sum of all positive elements in the array.
    """

    # Sort the array in descending order using bubble sort
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Remove duplicates
    unique_elements = set()
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] in unique_elements:
            del arr[i]
        else:
            unique_elements.add(arr[i])

    # Calculate the sum of positive elements
    positive_sum = 0
    for num in arr:
        if num > 0:
            positive_sum += num

    return positive_sum