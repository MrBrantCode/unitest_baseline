"""
QUESTION:
Write a function named `count_numbers(N, M)` that takes two integers `N` and `M` as input. The function should return the number of integers from 1 to `N` where the sum of their digits is divisible by `M` and the number itself is also divisible by `M`.
"""

def count_numbers(N, M):
    """
    Counts the number of integers from 1 to N where the sum of their digits is divisible by M and the number itself is also divisible by M.

    Args:
        N (int): The upper limit of the range.
        M (int): The divisor.

    Returns:
        int: The number of integers that satisfy the given conditions.
    """
    count = 0

    for i in range(1, N + 1):
        if i % M == 0 and sum(int(digit) for digit in str(i)) % M == 0:
            count += 1

    return count