"""
QUESTION:
Implement a function named `next_fib` that takes two integers `n1` and `n2` as input and returns the next element in the Fibonacci series. The function should calculate the sum of `n1` and `n2` to generate the next element in the series. The function should return the calculated sum. 

Note that the function should not handle generating the entire Fibonacci series, but only the next element given two previous elements.
"""

def next_fib(n1, n2):
    n3 = n1 + n2
    return n3