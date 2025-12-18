"""
QUESTION:
Write a function `calc_fib(n)` that uses recursion to calculate the nth Fibonacci number, where n is a positive integer. The Fibonacci sequence is defined as: 
- The 1st Fibonacci number is 0
- The 2nd Fibonacci number is 1
- Every subsequent Fibonacci number is the sum of the two preceding ones.
"""

def calc_fib(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return calc_fib(n-1) + calc_fib(n-2)