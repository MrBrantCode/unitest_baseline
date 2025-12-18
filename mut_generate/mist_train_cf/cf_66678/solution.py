"""
QUESTION:
Write a function `fibonacciSum(n)` that calculates the sum of all numbers in the Fibonacci sequence less than the input value `n`, where the numbers can be divided by 3 or 5 and their unit digit is 3 or 7.
"""

def fibonacciSum(n):
    total_sum = 0
    a, b = 1, 1
    while a < n:
        if (a % 3 == 0 or a % 5 == 0) and (a % 10 == 3 or a % 10 == 7):
            total_sum += a
        a, b = b, a + b
    return total_sum