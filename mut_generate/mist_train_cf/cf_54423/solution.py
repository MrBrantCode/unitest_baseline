"""
QUESTION:
Write a function `f(n)` that calculates the sum of the squares of its digits, then use this function to find the cumulative sum of all numbers `n` within the range `0 < n < 10^20` where `f(n)` is a perfect square. The function should return the last nine digits of the cumulative sum. Note that brute-force iteration is impractical due to the large range, so an efficient algorithm is required.
"""

def f(n):
    sum_of_squares = sum(int(digit)**2 for digit in str(n))
    return sum_of_squares ** 0.5 == int(sum_of_squares ** 0.5)