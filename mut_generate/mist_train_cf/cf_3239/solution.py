"""
QUESTION:
Implement a function `bubble_sort(nums)` that takes a list of integers `nums` as input and returns the sorted list in increasing order, then reversed. Do not use any built-in sorting functions or libraries. The function should handle edge cases such as an empty list, a list with only one element, or a list with duplicate elements.
"""

def bubble_sort(nums):
    if len(nums) <= 1:
        return nums
    
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    
    return nums[::-1]