"""
QUESTION:
Write a function named `accumulative_sum` that calculates the sum of the cubed values of all integers inclusively ranging from 1 to a specified integer value n. The function should take one integer argument n and return the calculated sum. The solution should have a time complexity of O(1) or less.
"""

def accumulative_sum(n):
    return (n * (n + 1) // 2) ** 2