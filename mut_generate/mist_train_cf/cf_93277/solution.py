"""
QUESTION:
Write a recursive function `findSmallest` that takes an array of integers and returns the index of the smallest element. The function should handle arrays with duplicate elements and have a time complexity of O(log n). The function should not use any loops, only recursive calls.
"""

def findSmallest(arr, start, end):
    """
    Find the index of the smallest element in the given array.

    Args:
    arr (list): The input array of integers.
    start (int): The starting index of the array.
    end (int): The ending index of the array.

    Returns:
    int: The index of the smallest element in the array.
    """
    if start == end:
        return start

    mid = (start + end) // 2
    leftSmallest = findSmallest(arr, start, mid)
    rightSmallest = findSmallest(arr, mid + 1, end)

    if arr[leftSmallest] <= arr[rightSmallest]:
        return leftSmallest
    else:
        return rightSmallest