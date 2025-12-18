"""
QUESTION:
Write a function `harmonic_mean_prime` that calculates the harmonic mean of a list of prime numbers. The function should take a list of integers as input and return the harmonic mean of these numbers. Assume that the input list only contains prime numbers.
"""

def harmonic_mean_prime(nums):
    sum_reciprocal = sum(1/n for n in nums)
    harmonic_mean = len(nums) / sum_reciprocal
    return harmonic_mean