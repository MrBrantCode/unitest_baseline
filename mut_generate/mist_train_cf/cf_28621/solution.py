"""
QUESTION:
Implement a function `sum_of_squares` that takes a list of integers as input and returns the sum of the squares of each integer in the list. The input list will be provided as a series of space-separated integers, and the output should be a single integer representing the sum of the squares.
"""

def sum_of_squares(nums):
    return sum(x**2 for x in nums)