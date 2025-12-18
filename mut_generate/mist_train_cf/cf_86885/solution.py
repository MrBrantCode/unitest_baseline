"""
QUESTION:
Create a class with a method `sort_array` that sorts an array of numbers in increasing order without using built-in sorting functions (e.g., `sorted()` or `.sort()`) and achieves a space complexity of O(1) by not using extra memory apart from the input array.
"""

def sort_array(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums