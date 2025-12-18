"""
QUESTION:
Implement a function called `bubble_sort` that sorts an array in ascending order using the Bubble Sort algorithm. The function should not use any built-in sorting functions or libraries, have a time complexity of O(n^2), and a space complexity of O(1).
"""

def bubble_sort(arr):
    """
    Sorts an array in ascending order using the Bubble Sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array in ascending order.
    """
    n = len(arr)
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr