"""
QUESTION:
Implement the `insertionSort` function to sort an array in ascending order using the insertion sort algorithm. The input array is a list of integers, and the output should be the sorted list. The function should modify the original array. The array can contain duplicate elements.
"""

def insertionSort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr