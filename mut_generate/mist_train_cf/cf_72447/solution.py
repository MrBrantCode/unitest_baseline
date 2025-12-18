"""
QUESTION:
Write a function named `printf_count` that calculates the approximate number of times `printf()` is executed in a nested loop structure, where the outer loop runs from 1 to `n` multiplied by 3 in each iteration, and the inner loop runs from the current outer loop counter to `n`. The function should take one integer argument `n`.
"""

def printf_count(n):
    """
    Calculate the approximate number of times printf() is executed in a nested loop structure.

    Args:
        n (int): The upper limit of the inner loop.

    Returns:
        float: The approximate number of times printf() is executed.
    """
    return n * (n + 1) * 1.5 / 2