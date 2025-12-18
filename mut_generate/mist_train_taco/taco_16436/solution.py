"""
QUESTION:
You are given a grid with 2 rows and 3 columns of squares.
The color of the square at the i-th row and j-th column is represented by the character C_{ij}.
Write a program that prints YES if this grid remains the same when rotated 180 degrees, and prints NO otherwise.

-----Constraints-----
 - C_{i,j}(1 \leq i \leq 2, 1 \leq j \leq 3) is a lowercase English letter.

-----Input-----
Input is given from Standard Input in the following format:
C_{11}C_{12}C_{13}
C_{21}C_{22}C_{23}

-----Output-----
Print YES if this grid remains the same when rotated 180 degrees; print NO otherwise.

-----Sample Input-----
pot
top

-----Sample Output-----
YES

This grid remains the same when rotated 180 degrees.
"""

def is_grid_rotationally_symmetric(row1: str, row2: str) -> str:
    """
    Determines if the given 2x3 grid remains the same when rotated 180 degrees.

    Parameters:
    row1 (str): The first row of the grid, a string of length 3.
    row2 (str): The second row of the grid, a string of length 3.

    Returns:
    str: "YES" if the grid remains the same when rotated 180 degrees, "NO" otherwise.
    """
    if row1[0] == row2[2] and row1[2] == row2[0] and row1[1] == row2[1]:
        return 'YES'
    else:
        return 'NO'