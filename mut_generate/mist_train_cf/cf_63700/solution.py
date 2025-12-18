"""
QUESTION:
Develop a recursive function `fibonacci_series` that calculates the Fibonacci series value at a specified position `n` and another function `fibonacci_sequence` that returns the sequence of Fibonacci numbers up to and including that index. The functions should utilize memoization to optimize time complexity. The solution must be able to handle large indexes without causing maximum recursion limit errors.
"""

def fibonacci_series(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    else:
        memo[n] = fibonacci_series(n-1, memo) + fibonacci_series(n-2, memo)
        return memo[n]

def fibonacci_sequence(n):
    sequence = []
    for i in range(1, n+1):
        sequence.append(fibonacci_series(i))
    return sequence