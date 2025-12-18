"""
QUESTION:
You are given a rectangular board of M × N squares. Also you are given an unlimited number of standard domino pieces of 2 × 1 squares. You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:

1. Each domino completely covers two squares.

2. No two dominoes overlap.

3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions.

Input

In a single line you are given two integers M and N — board sizes in squares (1 ≤ M ≤ N ≤ 16).

Output

Output one number — the maximal number of dominoes, which can be placed.

Examples

Input

2 4


Output

4


Input

3 3


Output

4
"""

def max_dominoes(M: int, N: int) -> int:
    """
    Calculate the maximum number of 2x1 dominoes that can be placed on a MxN board.

    Parameters:
    M (int): The number of rows in the board.
    N (int): The number of columns in the board.

    Returns:
    int: The maximum number of dominoes that can be placed.
    """
    return (M * N) // 2