"""
QUESTION:
Implement a function called bubble_sort that takes a list of integers as input and returns the sorted list in ascending order. The function should sort the input list in-place without using any additional data structures or built-in sorting functions.
"""

def bubble_sort(arr):
    """
    Sorts the input list in ascending order using the Bubble Sort algorithm.

    Args:
    arr (list): A list of integers to be sorted.

    Returns:
    list: The sorted list in ascending order.
    """
    n = len(arr)
    for i in range(n):
        # Initialize a flag to track whether a swap occurred during a pass.
        swapped = False
        for j in range(n - i - 1):
            # Compare the current element with the next element.
            if arr[j] > arr[j + 1]:
                # Swap their positions if the current element is greater than the next element.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to true if a swap occurred.
                swapped = True
        # If no swaps occurred during a pass, the array is already sorted.
        if not swapped:
            break
    return arr