"""
QUESTION:
Write a function called `fibonacci` that calculates the nth number in the Fibonacci sequence using recursive functions and dynamic programming techniques, and a function called `fibonacci_sequence` that generates the first n numbers of the Fibonacci sequence. The `fibonacci` function should store previously calculated values in a dictionary to avoid redundant calculations and prevent potential stack overflow errors.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

def fibonacci_sequence(n):
    sequence = []
    for i in range(n):
        sequence.append(fibonacci(i))
    return sequence