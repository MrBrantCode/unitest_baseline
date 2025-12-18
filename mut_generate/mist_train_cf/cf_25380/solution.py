"""
QUESTION:
Write a function `foo` that calculates the sum of the last `n` elements of an array `A` using recursion, and determine its time complexity as a function of `n`. The function should take an array `A` and an integer `n` as input, where `n` is the number of elements to sum from the end of the array.
"""

def foo(A, n):
    """
    Calculate the sum of the last n elements of an array A using recursion.

    Args:
        A (list): The input array.
        n (int): The number of elements to sum from the end of the array.

    Returns:
        int: The sum of the last n elements of the array.
    """
    if n == 0 or not A:
        return 0
    if n > len(A):
        n = len(A)
    return A[-1] + foo(A[:-1], n - 1)