"""
QUESTION:
Design a function `sum_of_odd_cubes` that calculates the sum of the cubes of all the odd numbers in a given list of integers. The function should not use any built-in functions or libraries for mathematical operations and should have a time complexity of O(n), where n is the length of the input list.
"""

def sum_of_odd_cubes(nums):
    odd_cubes_sum = 0
    for num in nums:
        if num % 2 != 0:
            odd_cubes_sum += num ** 3
    return odd_cubes_sum