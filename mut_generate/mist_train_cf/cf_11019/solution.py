"""
QUESTION:
Write a function named `sort_descending` that takes a list of integers as input and returns the list sorted in descending order. The function should use the bubble sort algorithm.
"""

def sort_descending(nums):
    n = len(nums)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                
    return nums