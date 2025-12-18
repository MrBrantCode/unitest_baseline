"""
QUESTION:
Create a function called `fibonacci(n)` that generates the nth Fibonacci number using memoization. The function should store calculated Fibonacci values in a dictionary to avoid redundant calculations and achieve a time complexity of O(n).
"""

def fibonacci(n):
    memo = {0: 0, 1: 1}   # Create a dictionary to store already calculated values
    if n not in memo:
        # If not, calculate and store in "memo"
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]   # Return the value 