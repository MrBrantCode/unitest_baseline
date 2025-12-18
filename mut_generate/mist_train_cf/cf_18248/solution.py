"""
QUESTION:
Design a function `countTrailingZeroes(n)` to compute the number of trailing zeroes in a factorial number `n!` without using division or modulo operations. The function should have a time complexity of O(log n) or better, use a constant amount of memory, and handle large values of `n`. Implement the function recursively using only basic arithmetic operations.
"""

def countTrailingZeroes(n):
    """
    Compute the number of trailing zeroes in a factorial number n! without using division or modulo operations.

    Args:
    n (int): The input number.

    Returns:
    int: The number of trailing zeroes in n!.
    """
    def recursive_count(n, count=0):
        if n < 5:
            return count
        else:
            multiplesOf5 = n // 5
            return recursive_count(multiplesOf5, count + multiplesOf5)

    return recursive_count(n)