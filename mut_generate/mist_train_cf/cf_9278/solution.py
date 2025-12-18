"""
QUESTION:
Create a function `sort_list` that takes a list of integers as input, removes duplicates, and returns the list in ascending order without using any built-in sorting functions or libraries. The input list can contain duplicate numbers and the function should not modify the original list. The function should be efficient and correctly handle lists of varying lengths.
"""

def sort_list(nums):
    # Remove duplicates from the list
    nums = list(set(nums))

    # Bubble sort algorithm to sort the list
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums