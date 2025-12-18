"""
QUESTION:
Implement a function `evenFibonacciSum(limit)` that calculates the sum of all even Fibonacci numbers less than or equal to a given integer `limit`. The function should return the total sum as an integer. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. The input `limit` is a non-negative integer.
"""

def evenFibonacciSum(limit):
    # Initialize the first two Fibonacci numbers
    fib1, fib2 = 0, 1
    evenSum = 0

    # Calculate the Fibonacci sequence and sum the even numbers
    while fib2 <= limit:
        if fib2 % 2 == 0:
            evenSum += fib2
        fib1, fib2 = fib2, fib1 + fib2

    return evenSum