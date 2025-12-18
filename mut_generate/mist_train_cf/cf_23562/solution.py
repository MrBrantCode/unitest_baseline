"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of integers in increasing order. The function should take an array of integers as input and return the sorted array. The function must use the bubble sort algorithm.
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1] :
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums