"""
QUESTION:
Implement a recursive binary search function called `binary_search` that takes four parameters: a sorted array of integers, a target integer, and the low and high indices of the array's subsequence that should be searched. The function should return the index of the target integer if found or -1 if not found in the array. The array can be of any size, but it should be sorted in ascending order.
"""

# Recursive Binary Search
def binary_search(array, target, low, high):
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array, target, low, mid - 1)
        else:
            return binary_search(array, target, mid + 1, high)
    else:
        return -1