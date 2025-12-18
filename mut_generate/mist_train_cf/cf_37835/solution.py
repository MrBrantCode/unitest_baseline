"""
QUESTION:
Implement a function `fibonacci_binet(n: int) -> int` to calculate the nth Fibonacci number using Binet's formula, where `n` is a non-negative integer and the function returns the result as an integer. The function should use the golden ratio and the square root of 5 in its calculation, but should not use iterative or recursive methods to calculate the Fibonacci sequence. Note that the function may not yield correct results for `n` greater than 72 due to rounding errors.
"""

def fibonacci_binet(n: int) -> int:
    phi = 1.61803398875
    sqrt_5 = 5 ** 0.5
    return int((phi ** n - (1 - phi) ** n) / sqrt_5)