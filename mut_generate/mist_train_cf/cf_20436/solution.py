"""
QUESTION:
Create a function named `bubble_sort` that takes an array of distinct numbers and returns a sorted array from least to greatest. The input array will contain between 2 and 10^6 numbers, all in the range of -10^9 to 10^9. Do not use any built-in sorting functions or libraries.
"""

def entance(nums):
    n = len(nums)
    
    for i in range(n-1):
        swapped = False
        
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        
        if not swapped:
            break
    
    return nums