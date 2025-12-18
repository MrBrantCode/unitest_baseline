"""
QUESTION:
You are given a square grid with $n$ rows and $n$ columns, where each cell has a non-negative integer written in it. There is a chip initially placed at the top left cell (the cell with coordinates $(1, 1)$). You need to move the chip to the bottom right cell (the cell with coordinates $(n, n)$).

In one step, you can move the chip to the neighboring cell, but:

you can move only right or down. In other words, if the current cell is $(x, y)$, you can move either to $(x, y + 1)$ or to $(x + 1, y)$. There are two special cases:

if the chip is in the last column (cell $(x, n)$) and you're moving right, you'll teleport to the first column (to the cell $(x, 1)$);

if the chip is in the last row (cell $(n, y)$) and you're moving down, you'll teleport to the first row (to the cell $(1, y)$).

you cannot visit the same cell twice. The starting cell is counted visited from the beginning (so you cannot enter it again), and you can't leave the finishing cell once you visit it.

Your total score is counted as the sum of numbers in all cells you have visited. What is the maximum possible score you can achieve?


-----Input-----

The first line contains the single integer $n$ ($2 \le n \le 200$) — the number of rows and columns in the grid.

Next $n$ lines contains the description of each row of the grid. The $i$-th line contains $n$ integers $a_{i, 1}, a_{i, 2}, \dots, a_{i, n}$ ($0 \le a_{i, j} \le 10^9$) where $a_{i, j}$ is the number written in the cell $(i, j)$.


-----Output-----

Print one integer — the maximum possible score you can achieve.


-----Examples-----

Input
2
1 2
3 4
Output
8
Input
3
10 10 10
10 0 10
10 10 10
Output
80


-----Note-----

None
"""

def max_possible_score(n, grid):
    """
    Calculate the maximum possible score for moving a chip from the top-left to the bottom-right cell
    in a square grid with teleportation rules.

    Parameters:
    n (int): The number of rows and columns in the grid.
    grid (list of list of int): The square grid containing non-negative integers.

    Returns:
    int: The maximum possible score achievable.
    """
    total_sum = 0
    for row in grid:
        total_sum += sum(row)
    
    diagonal_elements = []
    for i in range(n):
        diagonal_elements.append(grid[i][n - i - 1])
    
    return total_sum - min(diagonal_elements)