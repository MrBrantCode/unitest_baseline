"""
QUESTION:
We have a grid with H rows and W columns, where all the squares are initially white.

You will perform some number of painting operations on the grid. In one operation, you can do one of the following two actions:

* Choose one row, then paint all the squares in that row black.
* Choose one column, then paint all the squares in that column black.



At least how many operations do you need in order to have N or more black squares in the grid? It is guaranteed that, under the conditions in Constraints, having N or more black squares is always possible by performing some number of operations.

Constraints

* 1 \leq H \leq 100
* 1 \leq W \leq 100
* 1 \leq N \leq H \times W
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


H
W
N


Output

Print the minimum number of operations needed.

Examples

Input

3
7
10


Output

2


Input

14
12
112


Output

8


Input

2
100
200


Output

2
"""

def minimum_operations_to_paint(H: int, W: int, N: int) -> int:
    """
    Calculate the minimum number of operations needed to paint at least N black squares
    in a grid with H rows and W columns.

    Parameters:
    - H (int): Number of rows in the grid.
    - W (int): Number of columns in the grid.
    - N (int): Minimum number of black squares required.

    Returns:
    - int: The minimum number of operations needed.
    """
    return min([(N + H - 1) // H, (N + W - 1) // W])