"""
QUESTION:
Create a function named `second_largest_index` that takes a list of positive integers as input and returns the index of the second largest number in the list. The list may contain duplicate numbers and will always have at least two numbers.
"""

def second_largest_index(nums):
    largest = float('-inf')
    second_largest = float('-inf')
    largest_index = 0
    second_largest_index = 0
    
    for i in range(len(nums)):
        if nums[i] > largest:
            second_largest = largest
            second_largest_index = largest_index
            largest = nums[i]
            largest_index = i
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]
            second_largest_index = i
            
    return second_largest_index