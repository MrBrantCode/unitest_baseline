"""
QUESTION:
Implement a function called "bubble_sort" that takes an array of integers as input and returns the sorted array in ascending order. The function should not use any built-in sorting functions or libraries and should be able to handle arrays of any length, including large input sizes, and arrays containing negative numbers or duplicates. The algorithm should have a time complexity of O(n^2) in the worst case. The function should only iterate through the array once during the sorting process, but it may use a nested loop structure.
"""

def bubble_sort(nums):
    n = len(nums)
    
    for i in range(n-1):
        swapped = False
        
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        
        if not swapped:
            break
    
    return nums