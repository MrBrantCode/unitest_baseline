"""
QUESTION:
Write a function `calculate_time_complexity(n)` that determines the time complexity of a given coded snippet with nested loops, where the inner loop starts from the current value of the outer loop index `i`.
"""

def calculate_time_complexity(n):
    """
    This function calculates the time complexity of a coded snippet with nested loops.
    
    The time complexity is given by the sum of the arithmetic series n + (n-1) + (n-2) + ... + 1,
    which is equivalent to n * (n + 1) / 2.

    Args:
        n (int): The number of iterations in the outer loop.

    Returns:
        int: The total number of iterations in the nested loops.
    """
    return n * (n + 1) // 2