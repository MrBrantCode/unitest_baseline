"""
QUESTION:
The Siruseri amusement park has a new attraction. It consists of a rectangular array of discs. Each disc is divided into four equal sectors and the four sectors are coloured with the colours Red, Blue, Green and Yellow (in some order). The ordering may be different in different discs. Here is a possible arrangment of the discs:

You start at the top left disc. Your task is to walk down to the bottom right disc. In each step, you can rotate the current disc by $90$ degrees in the clockwise direction or move to a neighbouring disc. However, you can move to a neighbouring disc only if adjacent sectors of these two discs have the same colour. For example, in the figure above, you can move from the disc at position ($1$, $1$) to either of its neighbours. However, from the disc at position ($1$, $2$) you can only move to the disc at position ($1$, $1$). If you wish to move from ($1$, $2$) to ($1$, $3$) then you would have to rotate this disc three times so that the colour (red) on the adjacent sectors are the same.
For each rotate move, a penalty point is added to the score. The aim is to reach the bottom right with as few penalty points as possible. For example, in the arrangement described in the above figure, the best possible score is $2$, corresponding to the following path: Move from ($1$, $1$) to ($2$, $1$). Move from ($2$, $1$) to ($2$, $2$). Rotate. Rotate. Move from ($2$, $2$) to ($2$, $3$). Move from ($2$, $3$) to ($1$, $3$). Move from ($1$, $3$) to ($1$, $4$). Finally, move from ($1$, $4$) to ($2$, $4$).
Your task is to determine the minimum number of penalty points required to go from the top left disc to the bottom right disc for the given arrangement of discs.

-----Input:-----
The first line contains two integers $M$ and $N$. $M$ is the number of rows and $N$ is the number of columns in the given arrangment. This is followed by $M \times N$ lines of input. Lines $2$ to $N+1$, describe the colours on the discs on the first row, Lines $N+2$ to $2 \cdot N+1$ describe the colours on discs in the second row and so on. Each of these lines contain a permutation of the set {R, G, B, Y} giving the colours in the top, right, bottom and left sectors in that order.

-----Output:-----
A single integer on a single line indicating the minimum number of penalty points required to go from the top left disc to the bottom right disc for the given arrangement of discs.

-----Constraints:-----
- In $80 \%$ of the input, $1 \leq M,N \leq 60$.
- In all the inputs $1 \leq M,N \leq 1000$.

-----Sample Input-----
2 4
G Y B R
B G R Y
G Y B R
G R B Y
B Y G R
G B R Y
B R G Y
B R G Y

-----Sample Output-----
2
"""

import queue as Q

def min_penalty_to_reach_bottom_right(M, N, grid):
    dp = [[float('inf')] * N for _ in range(M)]
    dp[M - 1][N - 1] = 0
    pq = Q.PriorityQueue()
    pq.put([dp[M - 1][N - 1], M - 1, N - 1])
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while not pq.empty():
        pop = pq.get()
        cx, cy = pop[1], pop[2]
        if (cx, cy) not in visited:
            visited.add((cx, cy))
            for k in range(4):
                nx, ny = cx + directions[k][0], cy + directions[k][1]
                if 0 <= nx < M and 0 <= ny < N and ((nx, ny) not in visited):
                    clr = grid[cx][cy][k]
                    ind = grid[nx][ny].index(clr)
                    cost = (k - (ind + 2) % 4) % 4
                    if dp[cx][cy] + cost < dp[nx][ny]:
                        dp[nx][ny] = dp[cx][cy] + cost
                        pq.put([dp[nx][ny], nx, ny])
    
    return dp[0][0]