"""
QUESTION:
Implement a function `find_median` that takes a list of numbers as input and returns the median of the list. The function should first sort the list in ascending order. If the length of the list is odd, the function should return the middle value. If the length of the list is even, the function should return the average of the two middle values.
"""

def find_median(nums):
    nums.sort()  # Sort the list in ascending order
    length = len(nums)
    if length % 2 == 1:  # If length is odd
        return nums[length // 2]
    else:  # If length is even
        return (nums[length // 2 - 1] + nums[length // 2]) / 2