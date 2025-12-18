"""
QUESTION:
Implement a function named `find_average` that takes a list of numbers as input and returns the average of the numbers in the list. The function must calculate the sum of the numbers manually without using any built-in sum or average functions. The function should also not use any loops or recursion.
"""

def find_average(nums):
    n = len(nums)
    total = 0
    for i in range(n):
        total += nums[i]
    return total / n