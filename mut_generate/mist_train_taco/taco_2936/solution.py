"""
QUESTION:
You are given a grid with $n$ rows and $m$ columns, where each cell has a positive integer written on it. Let's call a grid good, if in each row the sequence of numbers is sorted in a non-decreasing order. It means, that for each $1 \le i \le n$ and $2 \le j \le m$ the following holds: $a_{i,j} \ge a_{i, j-1}$.

You have to to do the following operation exactly once: choose two columns with indexes $i$ and $j$ (not necessarily different), $1 \le i, j \le m$, and swap them.

You are asked to determine whether it is possible to make the grid good after the swap and, if it is, find the columns that need to be swapped.


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 100$). Description of the test cases follows.

The first line of each test case contains two integers $n$ and $m$ ($1 \le n, m \le 2 \cdot 10^5$) — the number of rows and columns respectively.

Each of the next $n$ rows contains $m$ integers, $j$-th element of $i$-th row is $a_{i,j}$ ($1 \le a_{i,j} \le 10^9$) — the number written in the $j$-th cell of the $i$-th row.

It's guaranteed that the sum of $n \cdot m$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

If after the swap it is impossible to get a good grid, output $-1$.

In the other case output $2$ integers — the indices of the columns that should be swapped to get a good grid.

If there are multiple solutions, print any.


-----Examples-----

Input
5
2 3
1 2 3
1 1 1
2 2
4 1
2 3
2 2
2 1
1 1
2 3
6 2 1
5 4 3
2 1
1
2
Output
1 1
-1
1 2
1 3
1 1


-----Note-----

In the first test case the grid is initially good, so we can, for example, swap the first column with itself.

In the second test case it is impossible to make the grid good.

In the third test case it is needed to swap the first and the second column, then the grid becomes good.
"""

def can_make_grid_good(grid):
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    
    if n == 0 or m == 0:
        return (1, 1)  # An empty grid or a single column grid is trivially good
    
    # Check if the grid is already good
    def is_good_grid(grid):
        for row in grid:
            if not all(row[i] <= row[i + 1] for i in range(len(row) - 1)):
                return False
        return True
    
    if is_good_grid(grid):
        return (1, 1)  # The grid is already good, return any valid swap
    
    # Try swapping each pair of columns and check if the grid becomes good
    for i in range(m):
        for j in range(i, m):
            # Create a copy of the grid to swap columns
            swapped_grid = [row[:] for row in grid]
            for row in swapped_grid:
                row[i], row[j] = row[j], row[i]
            
            if is_good_grid(swapped_grid):
                return (i + 1, j + 1)  # Return 1-based indices
    
    return -1  # No valid swap found