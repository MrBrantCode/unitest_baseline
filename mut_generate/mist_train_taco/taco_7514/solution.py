"""
QUESTION:
Given an integer N not less than 3, find the sum of the interior angles of a regular polygon with N sides.

Print the answer in degrees, but do not print units.

Constraints

* 3 \leq N \leq 100

Input

Input is given from Standard Input in the following format:


N


Output

Print an integer representing the sum of the interior angles of a regular polygon with N sides.

Examples

Input

3


Output

180


Input

100


Output

17640
"""

def calculate_interior_angle_sum(N: int) -> int:
    """
    Calculate the sum of the interior angles of a regular polygon with N sides.

    Parameters:
    N (int): The number of sides of the polygon (3 ≤ N ≤ 100).

    Returns:
    int: The sum of the interior angles of the polygon in degrees.
    """
    return int(N * 180 - 360)