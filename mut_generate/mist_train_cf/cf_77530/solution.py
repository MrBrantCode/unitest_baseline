"""
QUESTION:
Write a function `calculate_sums_and_average` that takes an integer `n` as input, calculates the sum of all integers from 1 to `n`, the sum of all distinct multiples of 3 and 5 within that range, and returns these two sums along with their average.
"""

def calculate_sums_and_average(n):
    normal_sum = sum(range(1,n+1))
    multiple_sum = sum([i for i in range(1, n+1) if i % 3 == 0 or i % 5 == 0])
    average = (normal_sum + multiple_sum) / 2
    return normal_sum, multiple_sum, average