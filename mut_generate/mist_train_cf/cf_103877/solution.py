"""
QUESTION:
Implement a function `bubble_sort` that sorts an array of integers in ascending order using the Bubble Sort algorithm. The function should take a list of integers as input and return the sorted list. The Bubble Sort algorithm should repeatedly iterate through the list, comparing adjacent elements and swapping them if they are in the wrong order, until the list is sorted.
"""

def bubble_sort(arr):
    """
    Sorts an array of integers in ascending order using the Bubble Sort algorithm.

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
            
            # If we find an element that is greater than its adjacent element, then swap them
            if arr[j] > arr[j+1]:
                # Swap values
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Set the flag to True so we'll loop again
                swapped = True
        
        # If no two elements were swapped in inner loop, the list is sorted
        if not swapped:
            break
    
    return arr