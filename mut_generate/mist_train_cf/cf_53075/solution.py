"""
QUESTION:
Write a function `bubbleSortDescending` that takes an array of integers as input, sorts it in descending order without using pre-existing sort methods, and returns the largest number.
"""

def bubbleSortDescending(arr):
    """
    This function sorts an array of integers in descending order using bubble sort and returns the largest number.
    
    Parameters:
    arr (list): A list of integers to be sorted
    
    Returns:
    int: The largest number in the sorted array
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

    return arr[0]