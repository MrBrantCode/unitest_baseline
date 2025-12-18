"""
QUESTION:
Implement a function `power(x, n)` that calculates the value of `x` raised to the power of `n` with a time complexity of O(log n). The function should handle boundary conditions where `n` can be zero or negative, and it should only accept integer values for `n`.
"""

def power(x, n):
    # base cases
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)

    # reduce the problem for even n
    elif n % 2 == 0:
        y = power(x, n / 2)
        return y * y

    # reduce the problem for odd n
    else:
        return x * power(x, n - 1)