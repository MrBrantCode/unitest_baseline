"""
QUESTION:
Implement a function `bubble_sort` to sort a list of numbers in increasing order without using any built-in sorting method. The function should have a time complexity of O(n^2) and a space complexity of O(1), where n is the number of elements in the list. The function should not use any additional data structures and should not modify the input list.
"""

def bubble_sort(arr):
    """
    Sorts a list of numbers in increasing order using the Bubble Sort algorithm.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Args:
        arr (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.
    """
    n = len(arr)

    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        
        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(n - i - 1):
            # If we find an element that is greater than its adjacent element, then swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True so we'll loop again
                swapped = True
        
        # If no two elements were swapped in inner loop, the list is sorted and we can terminate
        if not swapped:
            break

    return arr