"""
QUESTION:
Find the largest square number not exceeding N. Here, a square number is an integer that can be represented as the square of an integer.

-----Constraints-----
 - 1 \leq N \leq 10^9
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the largest square number not exceeding N.

-----Sample Input-----
10

-----Sample Output-----
9

10 is not square, but 9 = 3 × 3 is. Thus, we print 9.
"""

def find_largest_square_number(N: int) -> int:
    """
    Finds the largest square number not exceeding N.

    Parameters:
    N (int): The upper limit (1 ≤ N ≤ 10^9).

    Returns:
    int: The largest square number not exceeding N.
    """
    return int(N ** 0.5) ** 2