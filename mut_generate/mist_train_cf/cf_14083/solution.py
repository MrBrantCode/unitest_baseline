"""
QUESTION:
Implement a recursive function `fibonacci(n)` that finds the nth number in the Fibonacci sequence and computes the sum of all numbers in the sequence up to and including the nth number without using memoization. The function should take an integer `n` as input and return a tuple containing the nth number and the sum of all numbers up to the nth number.
"""

def entrance(n):
    if n <= 1:
        return (n, n)
    else:
        (a, sum_a) = entrance(n-1)
        (b, sum_b) = entrance(n-2)
        return (a+b, sum_a+sum_b+a)