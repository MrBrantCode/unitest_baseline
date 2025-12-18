"""
QUESTION:
Compute A + B.

Constraints

* -1000 ≤ A, B ≤ 1000

Input

The input will consist of a series of pairs of integers A and B separated by a space, one pair of integers per line. The input will be terminated by EOF.

Output

For each pair of input integers A and B, you must output the sum of A and B in one line.

Example

Input

1 2
10 5
100 20


Output

3
15
120
"""

def compute_sum(A: int, B: int) -> int:
    """
    Computes the sum of two integers A and B.

    Parameters:
    A (int): The first integer.
    B (int): The second integer.

    Returns:
    int: The sum of A and B.
    """
    return A + B