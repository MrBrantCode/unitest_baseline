"""
QUESTION:
Takahashi has a maze, which is a grid of H \times W squares with H horizontal rows and W vertical columns.
The square at the i-th row from the top and the j-th column is a "wall" square if S_{ij} is #, and a "road" square if S_{ij} is ..
From a road square, you can move to a horizontally or vertically adjacent road square.
You cannot move out of the maze, move to a wall square, or move diagonally.
Takahashi will choose a starting square and a goal square, which can be any road squares, and give the maze to Aoki.
Aoki will then travel from the starting square to the goal square, in the minimum number of moves required.
In this situation, find the maximum possible number of moves Aoki has to make.

-----Constraints-----
 - 1 \leq H,W \leq 20
 - S_{ij} is . or #.
 - S contains at least two occurrences of ..
 - Any road square can be reached from any road square in zero or more moves.

-----Input-----
Input is given from Standard Input in the following format:
H W
S_{11}...S_{1W}
:
S_{H1}...S_{HW}

-----Output-----
Print the maximum possible number of moves Aoki has to make.

-----Sample Input-----
3 3
...
...
...

-----Sample Output-----
4

If Takahashi chooses the top-left square as the starting square and the bottom-right square as the goal square, Aoki has to make four moves.
"""

def find_max_moves_in_maze(H, W, S):
    def BFS(M, i, j, H, W):
        if M[i][j] != '.':
            return 0
        to_visit = [{'row': i, 'col': j, 'step': 0}]
        checked = [[0] * W for _ in range(H)]
        checked[i][j] = 1
        z = [[0] * W for _ in range(H)]
        while to_visit:
            visiting = to_visit.pop(0)
            r0 = visiting['row']
            c0 = visiting['col']
            s0 = visiting['step']
            z[r0][c0] = s0
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                r = r0 + d[0]
                c = c0 + d[1]
                s = s0 + 1
                if checked[r][c] == 0 and M[r][c] == '.':
                    to_visit.append({'row': r, 'col': c, 'step': s})
                    checked[r][c] = 1
        a = 0
        for i in range(len(z)):
            for j in range(len(z[i])):
                if a < z[i][j]:
                    a = z[i][j]
        return a

    # Create a padded maze for easier boundary handling
    padded_maze = [['X'] * (W + 2)]
    for row in S:
        padded_maze.append(['X'] + list(row) + ['X'])
    padded_maze.append(['X'] * (W + 2))

    max_moves = 0
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if padded_maze[i][j] == '.':
                moves = BFS(padded_maze, i, j, H + 2, W + 2)
                if moves > max_moves:
                    max_moves = moves

    return max_moves