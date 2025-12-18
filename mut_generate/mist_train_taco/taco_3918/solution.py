"""
QUESTION:
In Chefland, there is a monthly robots competition. In the competition, a grid table of N rows and M columns will be used to place robots. A cell at row i and column j in the table is called cell (i, j). To join this competition, each player will bring two robots to compete and each robot will be placed at a cell in the grid table. Both robots will move at the same time from one cell to another until they meet at the same cell in the table. Of course they can not move outside the table. Each robot has a movable range. If a robot has movable range K, then in a single move, it can move from cell (x, y) to cell (i, j) provided (|i-x| + |j-y| <= K). However, there are some cells in the table that the robots can not stand at, and because of that, they can not move to these cells. The two robots with the minimum number of moves to be at the same cell will win the competition.

Chef plans to join the competition and has two robots with the movable range K1 and K2, respectively. Chef does not know which cells in the table will be used to placed his 2 robots, but he knows that there are 2 cells (1, 1) and (1, M) that robots always can stand at. Therefore, he assumes that the first robot is at cell (1, 1) and the other is at cell (1, M). Chef wants you to help him to find the minimum number of moves that his two robots needed to be at the same cell and promises to give you a gift if he wins the competition. 

-----Input-----
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
-  The first line of each test case contains 4 space-separated integers N M K1 K2 denoting the number of rows and columns in the table and the movable ranges of the first and second robot of Chef.
-  The next N lines, each line contains M space-separated numbers either 0 or 1 denoting whether the robots can move to this cell or not (0 means robots can move to this cell, 1 otherwise). It makes sure that values in cell (1, 1) and cell (1, M) are 0.

-----Output-----
For each test case, output a single line containing the minimum number of moves that Chef’s 2 robots needed to be at the same cell. If they can not be at the same cell, print -1.

-----Constraints-----
- 1 ≤ T ≤ 10
- 1 ≤ N, M ≤ 100
- 0 ≤ K1, K2 ≤ 10

----- Subtasks -----
Subtask #1 : (25 points) 
-  K1 = K2 = 1 

Subtask # 2 : (75 points) 
Original Constraints

-----Example-----
Input:
2
4 4 1 1
0 1 1 0
0 1 1 0
0 1 1 0
0 0 0 0
4 4 1 1
0 1 1 0
0 1 1 0
0 1 1 0
1 0 0 1

Output:
5
-1

-----Explanation-----
Example case 1. Robot 1 can move (1, 1) -> (2, 1) -> (3, 1) -> (4, 1) -> (4, 2) -> (4, 3), and robot 2 can move (1, 4) -> (2, 4) -> (3, 4) -> (4, 4) -> (4, 3) -> (4, 3), they meet at cell (4, 3) after 5 moves.
Example case 2. Because the movable range of both robots is 1, robot 1 can not move from (3, 1) to (4, 2), and robot 2 can not move from (3, 4) to (4, 3. Hence, they can not meet each other.
"""

import sys

def find_min_moves_to_meet(N, M, K1, K2, grid):
    def spaces(a, n, m, k, visit1, visit2, dist, position):
        queue = [position]
        lastedit = []
        dist[position[0]][position[1]] = 0
        while queue:
            point = queue[0]
            i, j = point
            if not visit1[i][j]:
                visit1[i][j] = True
                startx = max(i - k, 0)
                endx = min(i + k, n - 1)
                for x in range(startx, endx + 1):
                    starty = max(0, j + abs(x - i) - k)
                    endy = min(m - 1, j - abs(x - i) + k)
                    for y in range(starty, endy + 1):
                        if a[x][y] == 0 and not visit1[x][y]:
                            if visit2[x][y]:
                                lastedit.append([x, y])
                            if dist[x][y] > dist[i][j] + 1:
                                dist[x][y] = dist[i][j] + 1
                                queue.append([x, y])
            queue = queue[1:]
        return lastedit

    value = sys.maxsize
    listing = []
    visit1 = [[False for _ in range(M)] for _ in range(N)]
    visit2 = [[False for _ in range(M)] for _ in range(N)]
    dist1 = [[sys.maxsize for _ in range(M)] for _ in range(N)]
    dist2 = [[sys.maxsize for _ in range(M)] for _ in range(N)]

    if K1 >= K2:
        spaces(grid, N, M, K1, visit1, visit2, dist1, [0, 0])
    else:
        spaces(grid, N, M, K2, visit1, visit2, dist1, [0, M - 1])
        listing = spaces(grid, N, M, K1, visit2, visit1, dist2, [0, 0])

    if K1 > K2:
        listing = spaces(grid, N, M, K2, visit2, visit1, dist2, [0, M - 1])

    if K1 == K2:
        if dist1[0][M - 1] == sys.maxsize:
            return -1
        else:
            return int((dist1[0][M - 1] + 1) / 2)
    else:
        d = len(listing)
        for i in range(d - 1, -1, -1):
            x, y = listing[i]
            if visit1[x][y] and dist2[x][y] < value:
                value = dist2[x][y]
        return value if value != sys.maxsize else -1