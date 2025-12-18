"""
QUESTION:
Implement a function `insertion_sort(arr)` to sort an array of integers in ascending order without using built-in sorting methods. Then, implement a function `binary_search(arr, x)` to perform a binary search on the sorted array to find a specified integer. The `insertion_sort(arr)` function should return the sorted array and the `binary_search(arr, x)` function should return `True` if the integer is found and `False` otherwise. The time complexity for `insertion_sort(arr)` should be O(n^2) and for `binary_search(arr, x)` should be O(log n), with a space complexity of O(1) for both.
"""

def insertion_sort(arr):
    '''
    Sorting array in ascending order using Insertion Sort
    Args:
        arr: Unsorted array of integers
    Returns:
        Sorted array of integers in ascending order
    Complexity:
        Time: O(n^2)
        Space: O(1)
    '''
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def binary_search(arr, x):
    '''
    Searching value in array using Binary Search
    Args:
        arr: Sorted array of integers
        x: Integer to be searched
    Returns:
        True if integer is in array, else False
    Complexity:
        Time: O(log n)
        Space: O(1)
    '''
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return True

    return False