"""
QUESTION:
Create a function called `get_fib_term(n)` that generates the nth term in the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should take an integer `n` as input and return the corresponding Fibonacci term. The function should be able to handle cases where `n` is less than or equal to 1, as well as cases where `n` is greater than 1.
"""

def get_fib_term(n):
    if n <= 1:
        return n
    else:
        return get_fib_term(n-1) + get_fib_term(n-2)