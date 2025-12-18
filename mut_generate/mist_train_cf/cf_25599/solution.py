"""
QUESTION:
Write a function `myfunc(n)` with a time complexity analysis. The function should take an integer `n` as input and calculate the total number of iterations of a nested loop structure. The outer loop should iterate `n` times and the inner loop should also iterate `n` times. The function should return the total number of iterations. The time complexity of the function should be expressed using Big O notation.
"""

def myfunc(n):
    """
    Calculate the total number of iterations of a nested loop structure.

    The outer loop iterates n times and the inner loop also iterates n times.
    The time complexity of this function is O(n^2).

    Args:
        n (int): The number of iterations for the outer and inner loops.

    Returns:
        int: The total number of iterations.
    """
    total_iterations = 0
    for _ in range(n):  # Outer loop
        for _ in range(n):  # Inner loop
            total_iterations += 1
    return total_iterations