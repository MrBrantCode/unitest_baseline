"""
QUESTION:
Write a function named `find_median` that takes a list of integers as input and returns the median of the list as a floating-point number. The input list can contain both positive and negative integers, may not be sorted, and has a length between 1 and 10^5 inclusive. The function should handle both even and odd-sized lists and should not use any built-in libraries or functions.
"""

def find_median(nums):
    def partition(nums, low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
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

    n = len(nums)
    median_index = n // 2
    if n % 2 == 0:  
        median = (quickselect(nums, 0, n - 1, median_index - 1) + quickselect(nums, 0, n - 1, median_index)) / 2
    else:  
        median = quickselect(nums, 0, n - 1, median_index)
    return float(median)