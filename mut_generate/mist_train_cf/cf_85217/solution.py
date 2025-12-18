"""
QUESTION:
Write a function named `find_median` that calculates the median of an array of floating point numbers without using any library functions or methods for median calculations or sorting operations. The input array is not sorted and cannot be sorted using inbuilt sort function. The function should return the median value.
"""

def find_median(nums):
    length = len(nums)
    for i in range(length):
        for j in range(0, length - i - 1): 
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] 
    median = 0
    if length % 2 == 0: 
        median = (nums[length//2] + nums[length//2 - 1]) / 2.0
    else: 
        median = nums[length//2]
    return median