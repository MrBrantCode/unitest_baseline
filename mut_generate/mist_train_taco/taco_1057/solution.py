"""
QUESTION:
You are given a square grid with $n$ rows and $n$ columns. Each cell contains either $0$ or $1$.

In an operation, you can select a cell of the grid and flip it (from $0 \to 1$ or $1 \to 0$). Find the minimum number of operations you need to obtain a square that remains the same when rotated $0^{\circ}$, $90^{\circ}$, $180^{\circ}$ and $270^{\circ}$.

The picture below shows an example of all rotations of a grid.


-----Input-----

The first line contains a single integer $t$ ($1 \leq t \leq 100$) — the number of test cases.

The first line of each test case contains a single integer $n$ ($1 \leq n \leq 100$) — the size of the grid.

Then $n$ lines follow, each with $n$ characters $a_{i,j}$ ($0 \leq a_{i,j} \leq 1$) — the number written in each cell.


-----Output-----

For each test case output a single integer  — the minimum number of operations needed to make the square look the same rotated $0^{\circ}$, $90^{\circ}$, $180^{\circ}$ and $270^{\circ}$.


-----Examples-----

Input
5
3
010
110
010
1
0
5
11100
11011
01011
10011
11000
5
01000
10101
01010
00010
01001
5
11001
00000
11111
10110
01111
Output
1
0
9
7
6


-----Note-----

In the first test case, we can perform one operations to make the grid $\begin{matrix}0 & 1 & 0\\ 1 & 1 & {1}\\ 0 & 1 & 0\end{matrix}$. Now, all rotations of the square are the same.

In the second test case, all rotations of the square are already the same, so we don't need any flips.
"""

def min_operations_to_symmetric_grid(grid, n):
    """
    Calculate the minimum number of operations needed to make the grid look the same
    under 0°, 90°, 180°, and 270° rotations.

    Parameters:
    - grid (list of str): A list of strings where each string represents a row in the grid.
    - n (int): The size of the grid (number of rows and columns).

    Returns:
    - int: The minimum number of operations needed.
    """
    def count_flips(j, k):
        b = 0
        if grid[j][k] == '1':
            b += 1
        if grid[n - 1 - k][j] == '1':
            b += 1
        if grid[n - 1 - j][n - 1 - k] == '1':
            b += 1
        if grid[k][n - 1 - j] == '1':
            b += 1
        return b

    ans = 0
    if n % 2 == 1:
        # Odd case
        for j in range(int((n + 1) / 2)):
            for k in range(int((n - 1) / 2)):
                b = count_flips(j, k)
                if b == 1 or b == 3:
                    ans += 1
                elif b == 2:
                    ans += 2
    else:
        # Even case
        for j in range(int(n / 2)):
            for k in range(int(n / 2)):
                b = count_flips(j, k)
                if b == 1 or b == 3:
                    ans += 1
                elif b == 2:
                    ans += 2

    return ans