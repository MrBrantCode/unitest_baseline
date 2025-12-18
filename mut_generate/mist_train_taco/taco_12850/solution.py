"""
QUESTION:
How many ways are there to choose two distinct positive integers totaling N, disregarding the order?

Constraints

* 1 \leq N \leq 10^6
* N is an integer.

Input

Input is given from Standard Input in the following format:


N


Output

Print the answer.

Examples

Input

4


Output

1


Input

999999


Output

499999
"""

def count_ways_to_choose_two_integers(N: int) -> int:
    """
    Counts the number of ways to choose two distinct positive integers that sum to N.

    Parameters:
    N (int): The sum of the two distinct positive integers.

    Returns:
    int: The number of ways to choose the two distinct positive integers.
    """
    return N // 2 - int(N % 2 == 0)