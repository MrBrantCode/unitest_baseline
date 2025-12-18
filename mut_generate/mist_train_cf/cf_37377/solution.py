"""
QUESTION:
Implement the `find_median` function, which takes a sorted list of integers as input and returns the median value. The median is the middle value in an ordered integer list; if the list has an even number of elements, the median is the average of the two middle values. The input list is guaranteed to be sorted in ascending order.
"""

def find_median(nums):
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]