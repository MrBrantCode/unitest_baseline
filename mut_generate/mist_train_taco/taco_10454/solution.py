"""
QUESTION:
Pak Chanek has a grid that has $N$ rows and $M$ columns. Each row is numbered from $1$ to $N$ from top to bottom. Each column is numbered from $1$ to $M$ from left to right.

Each tile in the grid contains a number. The numbers are arranged as follows:

Row $1$ contains integers from $1$ to $M$ from left to right.

Row $2$ contains integers from $M+1$ to $2 \times M$ from left to right.

Row $3$ contains integers from $2 \times M+1$ to $3 \times M$ from left to right.

And so on until row $N$.

A domino is defined as two different tiles in the grid that touch by their sides. A domino is said to be tight if and only if the two numbers in the domino have a difference of exactly $1$. Count the number of distinct tight dominoes in the grid.

Two dominoes are said to be distinct if and only if there exists at least one tile that is in one domino, but not in the other.


-----Input-----

The only line contains two integers $N$ and $M$ ($1 \leq N, M \leq 10^9$) — the number of rows and columns in the grid.


-----Output-----

An integer representing the number of distinct tight dominoes in the grid.


-----Examples-----

Input
3 4
Output
9
Input
2 1
Output
1


-----Note-----

The picture below is the grid that Pak Chanek has in the first example.

The picture below is an example of a tight domino in the grid.
"""

def count_tight_dominoes(N: int, M: int) -> int:
    """
    Counts the number of distinct tight dominoes in a grid with N rows and M columns.

    Parameters:
    N (int): The number of rows in the grid.
    M (int): The number of columns in the grid.

    Returns:
    int: The number of distinct tight dominoes in the grid.
    """
    if M == 1:
        return N - 1
    else:
        return (M - 1) * N