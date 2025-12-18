"""
QUESTION:
Create a function called binary_search that takes in three parameters: the sorted array (arr), the target element (target), and the ending index of the search range (end). The function should return the index of the target element if found, and -1 otherwise. The function should implement a binary search approach and should not modify the input array. The input array is guaranteed to be sorted in ascending order.
"""

def binary_search(arr, target, end):
    start = 0
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return -1