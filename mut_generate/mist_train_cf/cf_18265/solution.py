"""
QUESTION:
Create a function bubbleSort(arr) that takes an array arr as input and sorts it in descending order. Implement a flag to check if the array is already sorted before the completion of the sorting algorithm. The function should return the sorted array.
"""

def bubbleSort(arr):
    """
    Sorts an array in descending order using the Bubble Sort algorithm.

    Args:
    arr (list): The input array to be sorted.

    Returns:
    list: The sorted array in descending order.
    """
    n = len(arr)
    for i in range(n):
        isSorted = True
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                isSorted = False
        if isSorted:
            break
    return arr