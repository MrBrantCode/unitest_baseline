"""
QUESTION:
Implement a function `solve(n, m)` that takes two integers `n` and `m` as input, where `n` is an odd integer between 1 and 7, and returns a string indicating whether the factorial of `n` is divisible by `m`. If `n` is not an odd integer between 1 and 7, return an error message.
"""

def solve(n, m):
    if n < 1 or n > 7 or n % 2 == 0:
        return 'The number must be an odd integer between 1 and 7.'
    else:
        factorial_n = 1
        for i in range(1, n+1):
            factorial_n *= i
        if factorial_n % m == 0:
            return f'The factorial of {n} is {factorial_n}, which is divisible by {m}.'
        else:
            return f'The factorial of {n} is {factorial_n}, which is not divisible by {m}.'