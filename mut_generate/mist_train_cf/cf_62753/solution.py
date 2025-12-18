"""
QUESTION:
Write a function called `fibo_sum` that calculates and returns the sum of all Fibonacci numbers smaller than the input number `n` that are divisible by 3 or 5 and have a last digit of 3 or 7. The function should use a Fibonacci sequence algorithm and check each number's divisibility and last digit conditions to include it in the sum.
"""

def fibo_sum(n):
    # first two numbers in fibonacci sequence
    x, y = 0, 1
    total = 0
    while y < n:
        x, y = y, x+y
        last_digit = y % 10
        if y < n and (last_digit == 3 or last_digit == 7) and (y % 3 == 0 or y % 5 == 0):
            total += y
    return total