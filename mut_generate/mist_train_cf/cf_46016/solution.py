"""
QUESTION:
Design a function named `fibonacci` that takes an integer `n` and an optional dictionary `memo` as input. The function should return a list of Fibonacci numbers up to the `n`th term. Implement memoization to optimize time complexity and handle larger Fibonacci numbers without leading to a stack overflow.
"""

def fibonacci(n, memo={}):
    # base case
    if n <= 0:
        return []
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # check if result already computed
    if n in memo:
        return memo[n]

    # recursive case
    previous_fibonacci = fibonacci(n - 1, memo)
    # next Fibonacci number is the sum of the last two numbers
    next_fibonacci = sum(previous_fibonacci[-2:])
    
    # save the result in cache before returning it
    memo[n] = previous_fibonacci + [next_fibonacci]

    return memo[n]