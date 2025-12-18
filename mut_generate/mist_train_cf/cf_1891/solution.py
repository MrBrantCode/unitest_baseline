"""
QUESTION:
Write a function called `find_median` that takes a list of numbers as input and returns the median. The function should have a time complexity of O(n log n) and a space complexity of O(1). The function should handle an empty list and lists containing both positive and negative numbers, as well as duplicate numbers.
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