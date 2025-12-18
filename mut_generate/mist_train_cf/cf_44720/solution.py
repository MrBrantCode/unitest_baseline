"""
QUESTION:
Create a function called `fibonacci(n)` that generates the first `n` numbers of the Fibonacci sequence, where each number is the sum of the two preceding numbers, and returns them as a list. The function should start with the initial two numbers in the sequence, 0 and 1, and continue adding numbers to the list until its length is `n`.
"""

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]