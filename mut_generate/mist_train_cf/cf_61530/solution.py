"""
QUESTION:
Implement a function named `power(x, n)` that calculates the result of x multiplied by itself n times without using the built-in power function or simple multiplication. The function should achieve a logarithmic time complexity by using recursion. The function should work for both positive and negative values of x and n, and should return 1/x^n when n is negative.
"""

def power(x, n):
    # Base case when n is 0, return 1
    if n == 0:
        return 1
    elif n < 0:
        # If n is negative, compute the inverse of the positive result
        return 1 / power(x, -n)
    else:
        # Otherwise divide n by 2 and multiply results
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x  # If n is odd, multiply an extra x
        return result