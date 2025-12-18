"""
QUESTION:
Problem

Given the integer n, output the smallest m such that nCm (the number of combinations that choose m out of n different ones) is even.

Constraints

The input satisfies the following conditions.

* 1 ≤ n ≤ 1018

Input

The input is given in the following format.


n


Output

Output the minimum m such that nCm is an even number on one line.

Examples

Input

2


Output

1


Input

111


Output

16


Input

3


Output

4
"""

def find_smallest_even_combination(n: int) -> int:
    """
    Finds the smallest m such that nCm (the number of combinations that choose m out of n different ones) is even.

    Parameters:
    n (int): The total number of items (1 ≤ n ≤ 10^18).

    Returns:
    int: The smallest m such that nCm is an even number.
    """
    return n + 1 & -(n + 1)