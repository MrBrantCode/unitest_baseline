"""
QUESTION:
Takahashi is standing on a two-dimensional plane, facing north. Find the minimum positive integer K such that Takahashi will be at the starting position again after he does the following action K times:

* Go one meter in the direction he is facing. Then, turn X degrees counter-clockwise.

Constraints

* 1 \leq X \leq 179
* X is an integer.

Input

Input is given from Standard Input in the following format:


X


Output

Print the number of times Takahashi will do the action before he is at the starting position again.

Examples

Input

90


Output

4


Input

1


Output

360
"""

from math import gcd

def find_minimum_K(X: int) -> int:
    """
    Finds the minimum positive integer K such that Takahashi will be at the starting position again
    after he does the following action K times:
    - Go one meter in the direction he is facing.
    - Then, turn X degrees counter-clockwise.

    Parameters:
    X (int): The degrees Takahashi turns counter-clockwise after each step.

    Returns:
    int: The minimum positive integer K.
    """
    g = gcd(X, 360)
    return 360 // g