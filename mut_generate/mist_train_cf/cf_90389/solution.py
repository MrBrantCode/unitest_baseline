"""
QUESTION:
Implement a function `find_median(nums)` that calculates the median of a list of integers without using any built-in functions or libraries for sorting or calculating the length of the list. Assume the list always has an odd number of elements, resulting in a unique median value. The function should have a time complexity of O(nlogn), where n is the length of the list.
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
    count = 0
    for _ in nums:
        count += 1
    median_index = count // 2
    return quickselect(nums, 0, count - 1, median_index)