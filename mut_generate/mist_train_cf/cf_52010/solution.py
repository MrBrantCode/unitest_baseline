"""
QUESTION:
Create a function that takes a set of integers as input, creates a copy of the set, and then iterates over the copied set to perform the following operations:

- For each integer in the set that is divisible by 2, calculate its factorial.
- For each integer in the set that is not divisible by 2, calculate the Fibonacci series up to that number.

The function should return the copied set and a dictionary containing the original integers as keys and the calculated results as values.
"""

import math

def fibonacci(n):
    a = 0
    b = 1
    fib_series = []
    while a <= n:
        fib_series.append(a)
        a, b = b, a+b
    return fib_series

def entance(my_set):
    copied_set = my_set.copy()
    results = {}
    for i in copied_set:
        if i % 2 == 0:
            results[i] = math.factorial(i)
        else:
            results[i] = fibonacci(i)
    return copied_set, results