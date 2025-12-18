"""
QUESTION:
Implement a function `tripfib(n)` that calculates the n-th element of the TripFib sequence, where `tripfib(n) == tripfib(n-1) + tripfib(n-2) + tripfib(n-3)` for `n > 2`, and `tripfib(0) == 0`, `tripfib(1) == 0`, `tripfib(2) == 1`. The function should accept an integer `n` with a maximum value of 20,000, and return "Invalid input" for non-integer inputs.
"""

def tripfib(n: float):
    if not isinstance(n, int):
        return 'Invalid input.'

    if n < 3:
        return [0, 0, 1][n]

    a, b, c = 0, 0, 1
    for _ in range(3, n+1):
        a, b, c = b, c, a+b+c
    return c