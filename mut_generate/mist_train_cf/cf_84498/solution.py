"""
QUESTION:
Write a function `rotated_array_search` that finds the index of a target element in a sorted and rotated array while maintaining a logarithmic time complexity of O(log n). The array may contain duplicate elements and the function should return -1 if the target element is not found or if the array is empty.
"""

def rotated_array_search(nums, target):
    if not nums:
        return -1

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:    # left half is sorted
            if nums[low] <= target < nums[mid]:    # target is in left half
                high = mid - 1
            else:
                low = mid + 1
        else:    # right half is sorted
            if nums[mid] < target <= nums[high]:    # target is in right half
                low = mid + 1
            else:
                high = mid - 1

    return -1