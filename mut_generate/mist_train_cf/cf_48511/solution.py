"""
QUESTION:
Write a function named `solve_recurrence_relation` that calculates the time complexity of the quicksort algorithm using the recurrence relation T(n) = 2T(n/2) + n. The function should take an integer `n` as input, representing the number of elements in the array, and return the calculated time complexity. Assume that the base case for the recurrence relation is T(1) = 1.
"""

def solve_recurrence_relation(n):
    """
    Calculate the time complexity of the quicksort algorithm using the recurrence relation T(n) = 2T(n/2) + n.

    Args:
    n (int): The number of elements in the array.

    Returns:
    int: The calculated time complexity.
    """
    if n <= 1:
        return 1  # base case: T(1) = 1
    else:
        return 2 * solve_recurrence_relation(n // 2) + n  # recursive case: T(n) = 2T(n/2) + n