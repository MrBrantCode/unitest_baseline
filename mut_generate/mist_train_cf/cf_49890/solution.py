"""
QUESTION:
Write a function called `fibonacciSums(n)` that calculates two sums of Fibonacci numbers less than `n`: the sum of the numbers that are divisible by 3 or 5 and end in either 3 or 7, and the sum of their squared values. The function should return these two sums as a list.
"""

def fibonacciSums(n):
    """
    Calculate two sums of Fibonacci numbers less than n:
    the sum of the numbers that are divisible by 3 or 5 and end in either 3 or 7,
    and the sum of their squared values.

    Args:
        n (int): The upper limit for Fibonacci numbers.

    Returns:
        list: A list containing two sums.
    """
    a, b = 0, 1
    total_sum = 0
    sum_squared = 0
    while b < n:
        a, b = b, a + b
        if b % 3 == 0 or b % 5 == 0:
            if b % 10 == 3 or b % 10 == 7:
                total_sum += b
                sum_squared += b ** 2
    return [total_sum, sum_squared]