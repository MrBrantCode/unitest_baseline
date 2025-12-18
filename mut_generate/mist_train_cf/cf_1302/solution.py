"""
QUESTION:
Implement a function `sort_array` that takes an array of numbers as input and sorts it in increasing order without using built-in sorting functions (e.g., sorted() or .sort()). The function should have a space complexity of O(1), only using the input array and a constant amount of extra memory.
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