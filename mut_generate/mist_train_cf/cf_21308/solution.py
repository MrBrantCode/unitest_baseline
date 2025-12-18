"""
QUESTION:
Generate a Fibonacci series up to the given positive integer `n` using a recursive function `fibonacci(n)`. The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

The function should satisfy the following conditions:
- Time complexity: O(n)
- Space complexity: O(1) (excluding the space used for the output)
- No loops or helper functions are allowed in the solution.
- Handle edge cases where `n` is 0 or 1, returning an empty list and a list containing only 0 respectively.
"""

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci(n - 1)
        series.append(series[-1] + series[-2])
        return series