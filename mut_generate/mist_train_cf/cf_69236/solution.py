"""
QUESTION:
Design a function named `fibonacci_sum(n)` that calculates the sum of all Fibonacci numbers less than or equal to the given number `n`, where `n` is a non-negative integer. The function should return 0 if `n` is less than or equal to 0.
"""

def fibonacci_sum(n):
    if n <= 0:
        return 0

    fibo_nums = [0, 1]  # Start with the first two numbers in the Fibonacci sequence
    while fibo_nums[-1] + fibo_nums[-2] <= n:
        fibo_nums.append(fibo_nums[-1] + fibo_nums[-2])  # Generate the next number in the sequence

    return sum(fibo_nums)