"""
QUESTION:
Implement a function called `find_first_occurrence` that finds the index of the first occurrence of a target element in a sorted array. The function should take in four parameters: a sorted array, the target element, and the low and high indices of the search range. The array may contain duplicate elements, and the function should return -1 if the target element is not found. The function must use a recursive approach and have a time complexity of O(log n), where n is the size of the array.
"""

def find_first_occurrence(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        if mid == 0 or arr[mid - 1] != target:
            return mid
        else:
            return find_first_occurrence(arr, target, low, mid - 1)
    elif arr[mid] < target:
        return find_first_occurrence(arr, target, mid + 1, high)
    else:
        return find_first_occurrence(arr, target, low, mid - 1)