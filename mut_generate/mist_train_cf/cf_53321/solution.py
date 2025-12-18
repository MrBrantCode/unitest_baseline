"""
QUESTION:
Write a function `bubble_sort_desc` that sorts an array of integers in descending order using the bubble sort algorithm. The function should take one argument, a list of integers, and return the sorted list. The function should not use any built-in sorting functions.
"""

def bubble_sort_desc(arr):
    """
    Sorts an array of integers in descending order using the bubble sort algorithm.

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
            # Compare the current item with its adjacent item
            if arr[j] < arr[j + 1]:
                # Swap values if the current item is smaller than its adjacent item
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True so we'll loop again
                swapped = True
        
        # If no two elements were swapped in inner loop, the array is sorted and we can terminate
        if not swapped:
            break
    
    return arr