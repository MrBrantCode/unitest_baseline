"""
QUESTION:
Write a function `maxNonAdjacentSum` that takes an array of integers as input and returns the maximum sum of non-adjacent elements in the array. The function should not include adjacent elements in the sum.
"""

def maxNonAdjacentSum(nums):
    incl = 0
    excl = 0
    for num in nums:
        new_excl = max(incl, excl)
        incl = excl + num
        excl = new_excl
    return max(incl, excl)