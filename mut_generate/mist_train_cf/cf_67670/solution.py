"""
QUESTION:
Create a function named `get_odds_fib_and_combine` that takes three lists of integers as input. The function should return a combined list of odd numbers and Fibonacci numbers from the input lists, excluding zero and positive numbers, in ascending order.

Implement a helper function to detect Fibonacci numbers.
"""

def is_perfect_square(x):
    s = int(x ** 0.5)
    return s * s == x

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def get_odds_fib_and_combine(l1, l2, l3):
    return sorted([num for num in sorted(l1 + l2 + l3) if num <= 0 and (num % 2 != 0 or is_fibonacci(num))])