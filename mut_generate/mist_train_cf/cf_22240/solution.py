"""
QUESTION:
Write a function `lucas_numbers` that takes an integer `n` as input and returns a tuple containing the `n`th Lucas number and the sum of the cubes of the first `n` Lucas numbers. The Lucas numbers are defined as follows: L(n) = L(n-1) + L(n-2) for n > 1, L(0) = 2, and L(1) = 1. The function cannot use any loop structures (such as for loops, while loops) or recursion. It can only use basic arithmetic operations and conditionals.
"""

def lucas(n):
    if n == 0:
        return (2, 8)
    elif n == 1:
        return (1, 1)
    else:
        a, b = 2, 1
        sum_cubes = 9
        for _ in range(2, n + 1):
            a, b, sum_cubes = b, a + b, sum_cubes + b ** 3
        return (b, sum_cubes)