"""
QUESTION:
Write a function `find_median(nums)` to calculate the median of a list of integers without using any built-in functions or libraries for sorting the list or calculating the length of the list. The function should have a time complexity of O(nlogn), where n is the length of the list. You can assume the list will always have an odd number of elements, so there will always be a unique median value.
"""

def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

def quickselect(nums, low, high, k):
    if low == high:
        return nums[low]

    pivot_index = partition(nums, low, high)
    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        return quickselect(nums, low, pivot_index - 1, k)
    else:
        return quickselect(nums, pivot_index + 1, high, k)

def find_median(nums):
    n = 0
    for _ in nums:
        n += 1
    median_index = (n - 1) // 2
    return quickselect(nums, 0, n - 1, median_index)