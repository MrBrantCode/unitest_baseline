"""
QUESTION:
Create a function `fibonacci(n, computed={0: 0, 1: 1})` that calculates the nth number in the Fibonacci sequence using memoization to avoid redundant calculations. The function should use recursion and store previously computed values in the `computed` dictionary.
"""

def fibonacci(n, computed = {0: 0, 1: 1}):
    # Check if the Fibonacci number is already computed
    if n not in computed:
        # Compute the n-th fibonacci number and store it
        computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
    # Return the n-th Fibonacci number
    return computed[n]