"""
QUESTION:
Design a Python function named `fib_in_range(A, B)` that generates all Fibonacci numbers within the inclusive range from A to B using dynamic programming. The function should take two integers A and B as input and return a list of Fibonacci numbers within the specified range. The goal is to optimize the solution for performance efficiency by leveraging the characteristics of the Fibonacci sequence.
"""

def fib_in_range(A, B):
    fib_range = []
    fib = [0, 1]
    while fib[-1] <= B:
        fib.append(fib[-1] + fib[-2])
    for num in fib:
        if num >= A and num <= B:
            fib_range.append(num)
    return fib_range