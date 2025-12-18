"""
QUESTION:
Write a function called `bubble_sort` that sorts an array of at least 1,000,000 positive integers from smallest to largest using the bubble sort algorithm.
"""

def bubble_sort(arr):
    """
    Sorts an array of integers from smallest to largest using the bubble sort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    n = len(arr)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(0, n-i-1):
            # If we find an element that is greater than its adjacent element then swap them
            if arr[j] > arr[j+1]:
                # Swap values
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Set the flag to True so we'll loop again
                swapped = True
        # If there were no swaps during the last iteration, the list is already sorted, and we can terminate
        if not swapped:
            break
    return arr