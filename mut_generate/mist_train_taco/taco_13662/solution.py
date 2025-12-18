"""
QUESTION:
There is a grid, consisting of $2$ rows and $m$ columns. The rows are numbered from $1$ to $2$ from top to bottom. The columns are numbered from $1$ to $m$ from left to right.

The robot starts in a cell $(1, 1)$. In one second, it can perform either of two actions:

move into a cell adjacent by a side: up, right, down or left;

remain in the same cell.

The robot is not allowed to move outside the grid.

Initially, all cells, except for the cell $(1, 1)$, are locked. Each cell $(i, j)$ contains a value $a_{i,j}$ — the moment that this cell gets unlocked. The robot can only move into a cell $(i, j)$ if at least $a_{i,j}$ seconds have passed before the move.

The robot should visit all cells without entering any cell twice or more (cell $(1, 1)$ is considered entered at the start). It can finish in any cell.

What is the fastest the robot can achieve that?


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of testcases.

The first line of each testcase contains a single integer $m$ ($2 \le m \le 2 \cdot 10^5$) — the number of columns of the grid.

The $i$-th of the next $2$ lines contains $m$ integers $a_{i,1}, a_{i,2}, \dots, a_{i,m}$ ($0 \le a_{i,j} \le 10^9$) — the moment of time each cell gets unlocked. $a_{1,1} = 0$. If $a_{i,j} = 0$, then cell $(i, j)$ is unlocked from the start.

The sum of $m$ over all testcases doesn't exceed $2 \cdot 10^5$.


-----Output-----

For each testcase, print a single integer — the minimum amount of seconds that the robot can take to visit all cells without entering any cell twice or more.


-----Examples-----

Input
4
3
0 0 1
4 3 2
5
0 4 8 12 16
2 6 10 14 18
4
0 10 10 10
10 10 10 10
2
0 0
0 0
Output
5
19
17
3


-----Note-----

None
"""

def calculate_minimum_time(m, row1, row2):
    # Ensure the first cell is marked as visited
    row1[0] = -1
    
    # Initialize dynamic time array
    dync = [0 for _ in range(m)]
    
    # Calculate dynamic times for even indices
    y = 0
    for x in range(m - 1):
        y = not y
        curr = max(row1[x] + 2, row1[x + 1] + 1) if y == 0 else max(row2[x] + 2, row2[x + 1] + 1)
        dync[x + 1] = max(curr, dync[x] + 2)
    
    # Calculate dynamic times for top row (even indices)
    top = list(range(0, m, 2))
    latestTime = 0
    for x in top[::-1]:
        dist = (m - x) * 2 - 1
        if x + 1 < m:
            curr = max(row1[x] + dist + 1, row1[x + 1] + dist, row2[x] + 1, row2[x + 1] + 2)
        else:
            curr = max(row1[x] + 2, row2[x] + 1)
        latestTime = max(latestTime + 2, curr)
        dync[x] = max(dync[x] + dist, latestTime)
    
    # Calculate dynamic times for bottom row (odd indices)
    bottom = list(range(1, m, 2))
    latestTime = 0
    for x in bottom[::-1]:
        dist = (m - x) * 2 - 1
        if x + 1 < m:
            curr = max(row2[x] + dist + 1, row2[x + 1] + dist, row1[x] + 1, row1[x + 1] + 2)
        else:
            curr = max(row2[x] + 2, row1[x] + 1)
        latestTime = max(latestTime + 2, curr)
        dync[x] = max(dync[x] + dist, latestTime)
    
    # Return the minimum time from the dynamic array
    return min(dync)