"""
QUESTION:
Write a function named `find_largest_number` that takes an array of integers as input and returns the largest number without using any built-in sorting or max functions. The function should iterate through the array to find the largest number.
"""

def entrance(nums):
    largest_number = nums[0]  # Assume the first number is the largest
    
    for num in nums:
        if num > largest_number:
            largest_number = num
    
    return largest_number