"""
QUESTION:
Write a function named `find_median` that calculates the median of a list of floating-point numbers. The function should sort the list and then determine the median based on whether the list length is even or odd. If the length is even, the median is the average of the two middle values; if it's odd, the median is the middle value. The function should be able to handle duplicate values in the list. The input list is not empty and contains only floating-point numbers.
"""

def find_median(nums):
    nums.sort()
    length = len(nums)
    middle = length // 2

    if length % 2 == 0:
        return (nums[middle - 1] + nums[middle]) / 2
    else:
        return nums[middle]