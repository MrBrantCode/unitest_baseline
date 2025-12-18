"""
QUESTION:
Compose a function `fibonacci(n)` that generates the nth Fibonacci number using recursion. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. Implement a list comprehension that uses `fibonacci(n)` to generate the first twenty numbers in the Fibonacci sequence, and handle possible overflow errors that may occur during calculation.
"""

def fibonacci(n, memo={}):
    if n in memo: return memo[n]
    if n <= 2: return min(n, 1)
    try:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result
    except OverflowError:
        print("An overflow error occured.")
        return