"""
QUESTION:
Write a function named `find_median` that takes a list of tuples, where each tuple contains an object id and its corresponding floating point value, and returns the median of these values. The input list is unsorted.
"""

def find_median(nums):
    # sort the list of tuples by the values
    nums.sort(key=lambda x: x[1])
    # fetch the values from the list of tuples
    vals = [i[1] for i in nums]
    n = len(vals)
    # if the count of the numbers is even
    if n % 2 == 0:
        # the median is the mean of the two middle elements
        median = (vals[n // 2 - 1] + vals[n // 2]) / 2
    else:
        # if the count of numbers is odd, the median is the middle element
        median = vals[n // 2]
    return median