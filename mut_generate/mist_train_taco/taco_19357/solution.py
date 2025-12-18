"""
QUESTION:
There is a rectangular room, covered with square tiles. Each tile is colored either red or black. A man is standing on a black tile. From a tile, he can move to one of four adjacent tiles. But he can't move on red tiles, he can move only on black tiles.

Write a program to count the number of black tiles which he can reach by repeating the moves described above.



Input

The input consists of multiple data sets. A data set starts with a line containing two positive integers W and H; W and H are the numbers of tiles in the x- and y- directions, respectively. W and H are not more than 20.

There are H more lines in the data set, each of which includes W characters. Each character represents the color of a tile as follows.

* '.' - a black tile
* '#' - a red tile
* '@' - a man on a black tile(appears exactly once in a data set)


The end of the input is indicated by a line consisting of two zeros.

Output

For each data set, your program should output a line which contains the number of tiles he can reach from the initial tile (including itself).

Examples

Input

6 9
....#.
.....#
......
......
......
......
......
#@...#
.#..#.
11 9
.#.........
.#.#######.
.#.#.....#.
.#.#.###.#.
.#.#..@#.#.
.#.#####.#.
.#.......#.
.#########.
...........
11 6
..#..#..#..
..#..#..#..
..#..#..###
..#..#..#@.
..#..#..#..
..#..#..#..
7 7
..#.#..
..#.#..
###.###
...@...
###.###
..#.#..
..#.#..
0 0


Output

45
59
6
13


Input

6 9
....#.
.....#
......
......
......
......
......
@...#
.#..#.
11 9
.#.........
.#.#######.
.#.#.....#.
.#.#.###.#.
.#.#..@#.#.
.#.#####.#.
.#.......#.
.#########.
...........
11 6
..#..#..#..
..#..#..#..
..#..#..###
..#..#..#@.
..#..#..#..
..#..#..#..
7 7
..#.#..
..#.#..
.###
...@...
.###
..#.#..
..#.#..
0 0


Output

45
59
6
13
"""

from collections import deque

def count_reachable_black_tiles(grid, start_pos):
    y = [-1, 0, 1, 0]
    x = [0, -1, 0, 1]
    
    def check(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])
    
    def bfs(a, b):
        res = 0
        d = deque()
        d.append([a, b])
        f = [[False] * len(grid[0]) for _ in range(len(grid))]
        while d:
            (i, j) = d.popleft()
            if not check(i, j):
                continue
            if grid[i][j] == '#':
                continue
            if f[i][j]:
                continue
            res += 1
            f[i][j] = True
            for k in range(4):
                d.append([i + y[k], j + x[k]])
        return res
    
    return bfs(start_pos[0], start_pos[1])