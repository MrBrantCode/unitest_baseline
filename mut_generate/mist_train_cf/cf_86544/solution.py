"""
QUESTION:
Implement a recursive sorting function named `quicksort` for a given array in Python. The array may contain both positive and negative integers. The implementation should not use any built-in sorting functions or libraries. The expected output for the given array [3, -2, 1, 4, -5] should be [-5, -2, 1, 3, 4]. The function should have a time complexity of O(n^2) and a space complexity of O(log n), where n is the size of the array, and be able to handle arrays with a maximum size of 10^6 elements.
"""

def quicksort(arr):
    """
    This function sorts an array using the quicksort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)