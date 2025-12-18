"""
QUESTION:
Create a function named `sum_of_odd_integers` that takes two parameters `n` and `m`, where `n` is the number of odd integers to sum and `m` is the starting odd integer. The function should return the sum of the first `n` odd integers starting from `m`.
"""

def sum_of_odd_integers(n, m):
    """
    This function calculates the sum of the first n odd integers starting from m.

    Args:
        n (int): The number of odd integers to sum.
        m (int): The starting odd integer.

    Returns:
        int: The sum of the first n odd integers starting from m.
    """
    total_sum = 0
    for i in range(m, m + (2 * n - 1), 2):
        total_sum += i
    return total_sum