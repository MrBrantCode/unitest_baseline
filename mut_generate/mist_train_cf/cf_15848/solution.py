"""
QUESTION:
Implement a function called binary_search_first that takes in a sorted list of integers and a target integer. The function should return the index of the first occurrence of the target in the list, or -1 if the target is not found. The list is sorted in ascending order and may contain duplicate integers. The function should use a binary search algorithm to find the target.
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