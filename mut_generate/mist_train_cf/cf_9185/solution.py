"""
QUESTION:
Write a function `double_sum` that calculates the sum of all the values in the input list `nums` and then doubles the sum. The function should take a list of integers as input and return an integer. The function should use a for loop to calculate the sum.
"""

def double_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total * 2