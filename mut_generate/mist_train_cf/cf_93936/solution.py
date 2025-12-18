"""
QUESTION:
Implement a function called `binary_search_first` that takes in a sorted list of integers `nums` and a target integer `target`. Return the index of the first occurrence of `target` in `nums`, or -1 if `target` is not found. Assume that the input list `nums` is sorted in ascending order and may contain duplicate elements.
"""

def binary_search_first(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = (low + high) // 2

        if nums[middle] == target:
            if middle == 0 or nums[middle - 1] != target:
                return middle
            else:
                high = middle - 1
        elif nums[middle] > target:
            high = middle - 1
        else:
            low = middle + 1

    return -1