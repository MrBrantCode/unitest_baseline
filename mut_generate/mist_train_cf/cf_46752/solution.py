"""
QUESTION:
Develop a Python function named `fibonacci` that generates the Fibonacci series up to the nth number. The function should take an integer `n` as input, verify that it is a positive integer, and return the series as a list of integers. The function should combine both iterative and recursive programming paradigms.
"""

def fibonacci(n):
    # Check if the input is positive integer
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"

    # Create a list to hold the series
    fib_series = [0, 1]

    # Recursive function to generate the series
    def recurse(n1, n2, count):
        if count < n:
            fib_series.append(n1 + n2)
            recurse(n2, n1+n2, count+1)

    # Kick off the recursion
    recurse(fib_series[-2], fib_series[-1], 2)

    return fib_series[:n]