"""
QUESTION:
Implement a recursive function named `fibonacci` that calculates the nth Fibonacci number. The function should take two parameters: `n` (the position of the Fibonacci number) and `memo` (a dictionary to store computed Fibonacci numbers for memoization). The function should return the nth Fibonacci number if `n` is a positive integer. If `n` is not a positive integer, the function should return an error message.
"""

def fibonacci(n, memo={}):
    # check if number is positive
    if n <= 0:
        return "Please input a positive integer."

    # check if number is in memo dictionary
    elif n in memo:
        return memo[n]

    # compute the fibonacci number
    else:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
            return memo[n]