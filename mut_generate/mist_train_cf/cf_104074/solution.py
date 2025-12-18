"""
QUESTION:
Implement a function called "bubble_sort" that takes an array of integers as input and returns the sorted array in ascending order. The function should handle arrays of any length, including those containing duplicate numbers and negative numbers, and should not use any built-in sorting functions or libraries. The function should be optimized to stop iterating as soon as the array is sorted.
"""

def bubble_sort(nums):
    n = len(nums)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        
        if not swapped:
            break
    
    return nums