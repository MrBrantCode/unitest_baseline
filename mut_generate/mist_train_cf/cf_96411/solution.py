"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth value of the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should return the correct value for any non-negative integer n.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]  # store previously calculated Fibonacci numbers
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]