"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of integers using the bubble sort algorithm. The function should have a time complexity of O(n^2) and a space complexity of O(1). It should be able to handle large arrays with up to 10^7 elements efficiently. The function should take an additional boolean parameter `ascending` to sort the array in either ascending (default) or descending order. It should handle duplicate elements correctly, maintain their relative order after sorting, and include proper error handling for invalid input or empty arrays.
"""

def bubble_sort(arr, ascending=True):
    """
    Sorts an array of integers using the bubble sort algorithm.

    Args:
    arr (list): The input array of integers.
    ascending (bool, optional): Whether to sort in ascending (True) or descending (False) order. Defaults to True.

    Returns:
    list: The sorted array.
    """

    # Check for empty array or invalid input
    if not arr or not isinstance(arr, list):
        return []

    n = len(arr)

    # Iterate through the array
    for i in range(n-1):
        # Flag to check if any swaps are made in a pass
        swapped = False

        # Compare adjacent elements and swap if necessary
        for j in range(n-i-1):
            if ascending:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            else:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True

        # If no swaps are made in a pass, the array is already sorted
        if not swapped:
            break

    return arr