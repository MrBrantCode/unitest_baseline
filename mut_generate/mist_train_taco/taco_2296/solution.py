"""
QUESTION:
For given integer n, count the totatives of n, that is, the positive integers less than or equal to n that are relatively prime to n.



Input


n


An integer n (1 ≤ n ≤ 1000000000).

Output

The number of totatives in a line.

Examples

Input

6


Output

2


Input

1000000


Output

400000
"""

def calculate_totatives(n: int) -> int:
    """
    Calculate the number of totatives of a given integer n.

    Parameters:
    n (int): The integer for which to calculate the totatives.

    Returns:
    int: The number of totatives of n.
    """
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = int(n / p)
            result -= int(result / p)
        p += 1
    if n > 1:
        result -= int(result / n)
    return result