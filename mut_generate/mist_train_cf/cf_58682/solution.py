"""
QUESTION:
Implement a function named `power` that takes two parameters: a numerical value `x` and an integer exponent `n`. The function should calculate the power of `x` elevated to `n` with a time complexity of O(log n). The function should also handle the cases where `n` is zero or negative.
"""

def power(x, n):
    if n == 0:
        return 1

    elif n < 0:
        return 1 / power(x, -n)

    else:
        if n % 2 == 0:
            temp = power(x, n // 2)
            return temp * temp

        else:
            temp = power(x, (n-1) // 2)
            return temp * temp * x