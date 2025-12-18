"""
QUESTION:
-----Input-----

The input contains a single integer a (10 ≤ a ≤ 999).


-----Output-----

Output 0 or 1.


-----Examples-----
Input
13

Output
1

Input
927

Output
1

Input
48

Output
0
"""

def is_odd(a: int) -> int:
    """
    Determines if the given integer is odd or even.

    Parameters:
    a (int): An integer between 10 and 999 (inclusive).

    Returns:
    int: 1 if the number is odd, 0 if the number is even.
    """
    return a % 2