"""
QUESTION:
Write a function `search(nums, target)` that searches for a `target` in a rotated array of integers `nums`. The array was originally sorted in ascending order and was rotated at some unknown pivot. If `target` exists, return its index; otherwise, return `-1`. The array has a length between 1 and 10^4, and all integers in `nums` are unique and between -9999 and 9999.
"""

def search(nums, target):
    if not nums:
        return -1

    # find the pivot
    def find_pivot(arr, low, high):
        if high < low:
            return 0
        if high == low:
            return low
        mid = (low + high)//2
        if mid < high and arr[mid] > arr[mid + 1]:
            return mid
        if mid > low and arr[mid] < arr[mid - 1]:
            return (mid-1)
        if arr[low] >= arr[mid]:
            return find_pivot(arr, low, mid - 1)
        return find_pivot(arr, mid + 1, high)

    # use binary search
    def binary_search(nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    pivot = find_pivot(nums, 0, len(nums) - 1)
    if nums[pivot] == target:
        return pivot
    if nums[0] <= target:
        return binary_search(nums, 0, pivot, target)
    return binary_search(nums, pivot + 1, len(nums) - 1, target)