"""
QUESTION:
Write a recursive function named `fib(n, memo = {})` that calculates the nth Fibonacci number using memoization, with the following restrictions: 
- If `n` is in `memo`, return the corresponding value from `memo`.
- If `n` is not in `memo`, calculate the value and store it in `memo` before returning it. 
- The Fibonacci sequence starts with numbers 1, 1.
"""

def fibonacci(n, memo = {}):
    # If n is in memo, it means it's already been computed
    if n in memo: 
        return memo[n]
    # If not, we need to compute it
    else:
        if n <= 2: 
            return 1
        else: 
            # Compute it, save it to the memo, and return it
            memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
            return memo[n]