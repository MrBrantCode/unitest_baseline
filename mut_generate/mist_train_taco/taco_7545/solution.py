"""
QUESTION:
A maze is composed of a grid of H \times W squares - H vertical, W horizontal.
The square at the i-th row from the top and the j-th column from the left - (i,j) - is a wall if S_{ij} is # and a road if S_{ij} is ..
There is a magician in (C_h,C_w). He can do the following two kinds of moves:
 - Move A: Walk to a road square that is vertically or horizontally adjacent to the square he is currently in.
 - Move B: Use magic to warp himself to a road square in the 5\times 5 area centered at the square he is currently in.
In either case, he cannot go out of the maze.
At least how many times does he need to use the magic to reach (D_h, D_w)?

-----Constraints-----
 - 1 \leq H,W \leq 10^3
 - 1 \leq C_h,D_h \leq H
 - 1 \leq C_w,D_w \leq W
 - S_{ij} is # or ..
 - S_{C_h C_w} and S_{D_h D_w} are ..
 - (C_h,C_w) \neq (D_h,D_w)

-----Input-----
Input is given from Standard Input in the following format:
H W
C_h C_w
D_h D_w
S_{11}\ldots S_{1W}
\vdots
S_{H1}\ldots S_{HW}

-----Output-----
Print the minimum number of times the magician needs to use the magic. If he cannot reach (D_h,D_w), print -1 instead.

-----Sample Input-----
4 4
1 1
4 4
..#.
..#.
.#..
.#..

-----Sample Output-----
1

For example, by walking to (2,2) and then using the magic to travel to (4,4), just one use of magic is enough.
Note that he cannot walk diagonally.
"""

from collections import deque

def min_magic_uses_to_reach_destination(H, W, C_h, C_w, D_h, D_w, maze):
    I = 9 ** 9
    d = [[I] * W for _ in range(H)]
    q = deque([(C_h - 1, C_w - 1, 0)])
    
    while q:
        y, x, c = q.popleft()
        if d[y][x] < I:
            continue
        d[y][x] = c
        for i in range(y - 2, y + 3):
            for j in range(x - 2, x + 3):
                if 0 <= i < H and 0 <= j < W and d[i][j] == I and maze[i][j] == '.':
                    if abs(y - i) + abs(x - j) < 2:
                        q.appendleft((i, j, c))
                    else:
                        q.append((i, j, c + 1))
    
    result = d[D_h - 1][D_w - 1]
    return result if result < I else -1