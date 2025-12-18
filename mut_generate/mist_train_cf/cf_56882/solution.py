"""
QUESTION:
Write a function `harmonic_mean` that calculates the harmonic mean of a list of numbers. The function should ignore zeros and negative numbers in the calculation. If all numbers are zeros or negatives, the function should return 0. The result should be rounded to two decimal places. The input list can contain any number of elements, but for this problem, it will always contain at least three numbers.
"""

def harmonic_mean(nums):
    count = len(nums)
    den_sum = sum([1/x if x > 0 else 0 for x in nums]) 
    if den_sum == 0:
        return 0 
    else:
        return round(count / den_sum, 2)