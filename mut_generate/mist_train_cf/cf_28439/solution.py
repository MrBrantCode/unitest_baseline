"""
QUESTION:
Implement a function called `tail_recursive_fibonacci` to calculate the nth Fibonacci number using tail recursion. The function should take two parameters: `n` (the index of the Fibonacci number to be calculated), and two optional parameters `a` and `b` with default values 0 and 1 respectively, representing the first two Fibonacci numbers. The function should return the calculated Fibonacci number and it should be able to handle inputs where n is 0 or 1 as base cases.
"""

def tail_recursive_fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return tail_recursive_fibonacci(n - 1, b, a + b)