"""
QUESTION:
Write a function `find_median(nums)` that calculates the median of a given list of numbers. The function should have a time complexity of O(n log n) and a space complexity of O(1). It should handle an empty list by returning None. The input list can contain both positive and negative numbers, be empty, or contain duplicate numbers.
"""

def find_median(nums):
    if len(nums) == 0:
        return None
    
    nums.sort()  # Sort the list in ascending order
    
    if len(nums) % 2 == 0:
        # If the length of the list is even, take the average of the two middle numbers
        middle_index = len(nums) // 2
        return (nums[middle_index - 1] + nums[middle_index]) / 2
    else:
        # If the length of the list is odd, return the middle number
        middle_index = len(nums) // 2
        return nums[middle_index]