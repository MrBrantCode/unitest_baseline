"""
QUESTION:
Write a function named `unique` that takes a list of integers as input and returns a new list containing the unique integers in sorted order from smallest to largest. The function should not use Python's built-in `sort` function or the `set` data structure.
"""

def unique(nums: list):
    # Remove duplicates
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                del nums[j]
            else:
                j+=1
        i+=1
             
    # Sort list
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums