"""
QUESTION:
Write a recursive function called `fibonacci` that calculates the nth number in the Fibonacci sequence and uses memoization to improve its efficiency. The function should take two parameters: `n` and `memo`, where `n` is the position of the Fibonacci number to calculate and `memo` is a dictionary that stores the results of previous calculations. The function should return the calculated Fibonacci number. The function should also include the base cases for the recursion, where `n` is 0 or 1.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        result = n
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    memo[n] = result
    return result