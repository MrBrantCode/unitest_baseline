"""
QUESTION:
Write a function named `deduct_ten` that takes an integer `x` as input and returns the result of subtracting 10 from `x` if `x` meets the following conditions: `x` is greater than 100, `x` is divisible by 5, `x` is not a prime number, and `x` is not a perfect square. Otherwise, return the original value of `x`.
"""

def deduct_ten(x):
    return x - 10 if x > 100 and x % 5 == 0 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and int(x**0.5 + 0.5)**2 != x else x