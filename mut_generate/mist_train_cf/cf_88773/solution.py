"""
QUESTION:
Write a function named `find_position` that takes two arguments: a sorted array `arr` and a number `num`. Using a recursive binary search algorithm, return the position of `num` in `arr` with a time complexity of O(log n), where n is the length of the array. If `num` is not found in `arr`, return -1.
"""

def find_position(arr, num):
    def binary_search(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            return binary_search(mid+1, high)
        else:
            return binary_search(low, mid-1)
    return binary_search(0, len(arr)-1)