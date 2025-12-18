"""
QUESTION:
Implement the bubble_sort function that sorts an array in ascending order using the Bubble Sort algorithm. The function should take an array of integers as input and return the sorted array.
"""

def bubble_sort(arr):
    """
    This function sorts an array in ascending order using the Bubble Sort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted list of integers in ascending order.
    """
    n = len(arr)
    
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        
        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(n - i - 1):
            # If we find an element that is greater than its adjacent element in the list
            if arr[j] > arr[j + 1]:
                # Swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True so we'll loop again after this iteration
                swapped = True
        
        # If there were no swaps during the last iteration, the list is already sorted, and we can terminate
        if not swapped:
            break
    
    return arr