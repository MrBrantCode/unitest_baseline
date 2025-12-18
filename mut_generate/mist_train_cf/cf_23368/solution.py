"""
QUESTION:
Implement a function called `bubble_sort_desc` to sort an array of integers in descending order using the Bubble Sort algorithm. The function should take an array of integers as input and return the sorted array. The array may contain duplicate elements.
"""

def bubble_sort_desc(arr):
    """
    Sorts an array of integers in descending order using the Bubble Sort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted list in descending order.
    """
    n = len(arr)
    
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        
        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(n - i - 1):
            # If we find an element that is smaller than its adjacent element, swap them
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True so we'll loop again
                swapped = True
        
        # If no two elements were swapped in the last iteration, the list is sorted
        if not swapped:
            break
    
    return arr