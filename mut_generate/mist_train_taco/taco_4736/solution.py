"""
QUESTION:
The main building of the nation is developing complex patterns as each day progresses.
The task is to find the number of three sided closed figures on the nth day.

(Input – n

Output – number of triangles)

SAMPLE INPUT
2

SAMPLE OUTPUT
5
"""

def calculate_triangles(n: int) -> int:
    """
    Calculate the number of three-sided closed figures (triangles) on the nth day.

    Parameters:
    n (int): The nth day.

    Returns:
    int: The number of triangles on the nth day.
    """
    return n * n + (n - 1) ** 2