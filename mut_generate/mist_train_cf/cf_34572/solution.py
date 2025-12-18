"""
QUESTION:
Implement a function `sum_divisible(arr, divisor)` that takes an array of integers `arr` and an integer `divisor` as input and returns the sum of all elements in `arr` that are divisible by `divisor`.
"""

def sum_divisible(arr, divisor):
    return sum(num for num in arr if num % divisor == 0)