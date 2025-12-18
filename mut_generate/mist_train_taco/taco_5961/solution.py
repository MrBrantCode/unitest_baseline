"""
QUESTION:
Mary has an $n\times m$ piece of paper that she wants to cut into $1\times1$ pieces according to the following rules:

She can only cut one piece of paper at a time, meaning she cannot fold the paper or layer already-cut pieces on top of one another. 
Each cut is a straight line from one side of the paper to the other side of the paper. For example, the diagram below depicts the three possible ways to cut a $3\times2$ piece of paper: 

Given $n$ and $m$, find and print the minimum number of cuts Mary must make to cut the paper into $n\cdot m$ squares that are $1\times1$ unit in size. 

Input Format

A single line of two space-separated integers denoting the respective values of $n$ and $m$.

Constraints

$1\leq n,m\leq10^9$

Output Format

Print a long integer denoting the minimum number of cuts needed to cut the entire paper into $1\times1$ squares.

Sample Input
3 1

Sample Output
2

Explanation

Mary first cuts the $3\times1$ piece of paper into a $1\times1$ piece and a $2\times1$ piece. She then cuts the $2\times1$ piece into two $1\times1$ pieces:

Because it took her two cuts to get $n\times m=3$ pieces of size $1\times1$, we print $2$ as our answer.
"""

def minimum_cuts(n: int, m: int) -> int:
    """
    Calculate the minimum number of cuts required to cut an n x m piece of paper into 1x1 pieces.

    Parameters:
    n (int): The number of rows in the paper.
    m (int): The number of columns in the paper.

    Returns:
    int: The minimum number of cuts required.
    """
    return n * m - 1