"""
QUESTION:
Write a function named `count_numbers` that takes two integers `N` and `M` as input. The function should return the number of integers from 1 to `N` (inclusive) where the sum of their digits is divisible by `M` and the number itself is also divisible by `M`.
"""

def sum_of_digits(num):
    """
    Helper function to calculate the sum of digits of a number.
    """
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

def count_numbers(N, M):
    count = 0
    for num in range(1, N+1):
        if num % M == 0 and sum_of_digits(num) % M == 0:
            count += 1
    return count