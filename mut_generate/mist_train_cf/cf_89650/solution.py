"""
QUESTION:
Implement a function `find_first_occurrence(arr, target)` to find the index of the first occurrence of a given target element in a sorted array `arr` containing duplicate elements. The array size can be up to 10^9 elements. The function should return -1 if the target element is not present in the array. The time complexity should be O(log n) and space complexity should be O(log n) in the worst case scenario, where n is the size of the input array.
"""

def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] < target:
                return mid
            else:
                high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1