"""
QUESTION:
Takahashi is locked within a building.

This building consists of H×W rooms, arranged in H rows and W columns. We will denote the room at the i-th row and j-th column as (i,j). The state of this room is represented by a character A_{i,j}. If A_{i,j}= `#`, the room is locked and cannot be entered; if A_{i,j}= `.`, the room is not locked and can be freely entered. Takahashi is currently at the room where A_{i,j}= `S`, which can also be freely entered.

Each room in the 1-st row, 1-st column, H-th row or W-th column, has an exit. Each of the other rooms (i,j) is connected to four rooms: (i-1,j), (i+1,j), (i,j-1) and (i,j+1).

Takahashi will use his magic to get out of the building. In one cast, he can do the following:

* Move to an adjacent room at most K times, possibly zero. Here, locked rooms cannot be entered.
* Then, select and unlock at most K locked rooms, possibly zero. Those rooms will remain unlocked from then on.



His objective is to reach a room with an exit. Find the minimum necessary number of casts to do so.

It is guaranteed that Takahashi is initially at a room without an exit.

Constraints

* 3 ≤ H ≤ 800
* 3 ≤ W ≤ 800
* 1 ≤ K ≤ H×W
* Each A_{i,j} is `#` , `.` or `S`.
* There uniquely exists (i,j) such that A_{i,j}= `S`, and it satisfies 2 ≤ i ≤ H-1 and 2 ≤ j ≤ W-1.

Input

Input is given from Standard Input in the following format:


H W K
A_{1,1}A_{1,2}...A_{1,W}
:
A_{H,1}A_{H,2}...A_{H,W}


Output

Print the minimum necessary number of casts.

Examples

Input

3 3 3
#.#
#S.
###


Output

1


Input

3 3 3
.#
S.


Output

1


Input

3 3 3

S#


Output

2


Input

7 7 2


...##
S###
.#.##
.###


Output

2
"""

from collections import deque

def minimum_casts_to_exit(H, W, K, A):
    # Find the starting position of Takahashi
    sx, sy = -1, -1
    for i in range(H):
        for j in range(W):
            if A[i][j] == 'S':
                sx, sy = i, j
                break
        if sx != -1:
            break
    
    # Initialize the visited matrix
    ma = [[0] * W for _ in range(H)]
    
    def dfs(x, y, z):
        if ma[x][y] == 1:
            return
        if z > K:
            return
        ma[x][y] = 1
        if x > 0 and A[x - 1][y] == '.':
            que.append([x - 1, y, z + 1])
        if y > 0 and A[x][y - 1] == '.':
            que.append([x, y - 1, z + 1])
        if x < H - 1 and A[x + 1][y] == '.':
            que.append([x + 1, y, z + 1])
        if y < W - 1 and A[x][y + 1] == '.':
            que.append([x, y + 1, z + 1])
    
    # Initialize the queue for BFS
    que = deque([[sx, sy, 0]])
    while que:
        x, y, z = que.popleft()
        dfs(x, y, z)
    
    # Calculate the minimum number of casts required to reach an exit
    ans = float('inf')
    for i in range(H):
        for j in range(W):
            if ma[i][j] == 1:
                ans = min(ans, 1 + (H - i - 1) // K + (1 if (H - i - 1) % K else 0), 
                          1 + (W - j - 1) // K + (1 if (W - j - 1) % K else 0), 
                          1 + i // K + (1 if i % K else 0), 
                          1 + j // K + (1 if j % K else 0))
    
    return ans