"""
QUESTION:
We have an N \times N square grid.
We will paint each square in the grid either black or white.
If we paint exactly A squares white, how many squares will be painted black?

-----Constraints-----
 - 1 \leq N \leq 100
 - 0 \leq A \leq N^2

-----Inputs-----
Input is given from Standard Input in the following format:
N
A

-----Outputs-----
Print the number of squares that will be painted black.

-----Sample Input-----
3
4

-----Sample Output-----
5

There are nine squares in a 3 \times 3 square grid.
Four of them will be painted white, so the remaining five squares will be painted black.
"""

def calculate_black_squares(N: int, A: int) -> int:
    """
    Calculate the number of squares that will be painted black in an N x N grid
    when exactly A squares are painted white.

    Parameters:
    - N (int): The size of the N x N grid.
    - A (int): The number of squares to be painted white.

    Returns:
    - int: The number of squares that will be painted black.
    """
    return N * N - A