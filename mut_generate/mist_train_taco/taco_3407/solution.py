"""
QUESTION:
You are playing some computer game. One of its levels puts you in a maze consisting of n lines, each of which contains m cells. Each cell either is free or is occupied by an obstacle. The starting cell is in the row r and column c. In one step you can move one square up, left, down or right, if the target cell is not occupied by an obstacle. You can't move beyond the boundaries of the labyrinth.

Unfortunately, your keyboard is about to break, so you can move left no more than x times and move right no more than y times. There are no restrictions on the number of moves up and down since the keys used to move up and down are in perfect condition.

Now you would like to determine for each cell whether there exists a sequence of moves that will put you from the starting cell to this particular one. How many cells of the board have this property?


-----Input-----

The first line contains two integers n, m (1 ≤ n, m ≤ 2000) — the number of rows and the number columns in the labyrinth respectively.

The second line contains two integers r, c (1 ≤ r ≤ n, 1 ≤ c ≤ m) — index of the row and index of the column that define the starting cell.

The third line contains two integers x, y (0 ≤ x, y ≤ 10^9) — the maximum allowed number of movements to the left and to the right respectively.

The next n lines describe the labyrinth. Each of them has length of m and consists only of symbols '.' and '*'. The j-th character of the i-th line corresponds to the cell of labyrinth at row i and column j. Symbol '.' denotes the free cell, while symbol '*' denotes the cell with an obstacle.

It is guaranteed, that the starting cell contains no obstacles.


-----Output-----

Print exactly one integer — the number of cells in the labyrinth, which are reachable from starting cell, including the starting cell itself.


-----Examples-----
Input
4 5
3 2
1 2
.....
.***.
...**
*....

Output
10

Input
4 4
2 2
0 1
....
..*.
....
....

Output
7



-----Note-----

Cells, reachable in the corresponding example, are marked with '+'.

First example:  

+++..

+***.

+++**

*+++.

 

Second example:  

.++.

.+*.

.++.

.++.
"""

from collections import deque

def count_reachable_cells(n, m, r, c, x, y, labyrinth):
    # Convert 1-based indices to 0-based
    r -= 1
    c -= 1
    
    # Initialize visited array and answer
    vd = [[0] * m for _ in range(n)]
    ans = 0
    
    # Initialize the queue for BFS
    to_visit = deque()
    to_visit.append((r, c, x, y))
    
    while to_visit:
        ri, ci, xi, yi = to_visit.popleft()
        
        # Move up
        ru = ri
        while ru >= 0 and labyrinth[ru][ci] == '.' and not vd[ru][ci]:
            vd[ru][ci] = 1
            ans += 1
            if xi > 0 and ci - 1 >= 0 and labyrinth[ru][ci - 1] == '.' and not vd[ru][ci - 1]:
                to_visit.append((ru, ci - 1, xi - 1, yi))
            if yi > 0 and ci + 1 < m and labyrinth[ru][ci + 1] == '.' and not vd[ru][ci + 1]:
                to_visit.append((ru, ci + 1, xi, yi - 1))
            ru -= 1
        
        # Move down
        rd = ri + 1
        while rd < n and labyrinth[rd][ci] == '.' and not vd[rd][ci]:
            vd[rd][ci] = 1
            ans += 1
            if xi > 0 and ci - 1 >= 0 and labyrinth[rd][ci - 1] == '.' and not vd[rd][ci - 1]:
                to_visit.append((rd, ci - 1, xi - 1, yi))
            if yi > 0 and ci + 1 < m and labyrinth[rd][ci + 1] == '.' and not vd[rd][ci + 1]:
                to_visit.append((rd, ci + 1, xi, yi - 1))
            rd += 1
    
    return ans