"""
QUESTION:
Implement a function `insertion_sort(arr)` that sorts a list of integers in non-decreasing order using the augmented binary search algorithm. The function should be able to handle duplicates and have a time complexity of O(n log n) in the best case and O(n^2) in the worst case. The input list `arr` contains n long integer elements and may be numerically dense.
"""

def binary_search(arr, val, start, end):
    """
    This is a helper function that performs a binary search
    It takes in an array and a value, starting and ending indices
    Returns the index where the value should be inserted in the array
    """
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
    elif start > end:
        return start

    mid = (start+end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

def insertion_sort(arr):
    """
    This is the insertion sort function that sorts an array
    It makes use of the binary_search helper function
    """
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr