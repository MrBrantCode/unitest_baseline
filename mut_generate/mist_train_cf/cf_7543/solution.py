"""
QUESTION:
Implement the function interpolation_search(arr, target) to find the position of a target number in a sorted list of integers (arr) using the interpolation search algorithm. The function should return the index of the target number if found, and -1 otherwise. The interpolation search algorithm should have a time complexity of O(log log n) and be able to handle a list of up to 1 million integers.
"""

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1