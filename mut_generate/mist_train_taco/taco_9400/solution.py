"""
QUESTION:
In this task Anna and Maria play a game with a very unpleasant rival. Anna and Maria are in the opposite squares of a chessboard (8 × 8): Anna is in the upper right corner, and Maria is in the lower left one. Apart from them, the board has several statues. Each statue occupies exactly one square. A square that contains a statue cannot have anything or anyone — neither any other statues, nor Anna, nor Maria.

Anna is present on the board as a figurant (she stands still and never moves), and Maria has been actively involved in the game. Her goal is — to come to Anna's square. Maria and statues move in turn, Maria moves first. During one move Maria can go to any adjacent on the side or diagonal cell in which there is no statue, or she can stay in the cell where she is. The statues during their move must go one square down simultaneously, and those statues that were in the bottom row fall from the board and are no longer appeared.

At that moment, when one of the statues is in the cell in which the Maria is, the statues are declared winners. At the moment when Maria comes into the cell where Anna has been waiting, Maria is declared the winner.

Obviously, nothing depends on the statues, so it all depends on Maria. Determine who will win, if Maria does not make a strategic error.

Input

You are given the 8 strings whose length equals 8, describing the initial position on the board. The first line represents the top row of the board, the next one — for the second from the top, and so on, the last line represents the bottom row. Each character string matches a single cell board in the appropriate row, and the characters are in the same manner as that of the corresponding cell. If the cell is empty, the corresponding character is ".". If a cell has Maria, then it is represented by character "M". If a cell has Anna, it is represented by the character "A". If a cell has a statue, then the cell is represented by character "S".

It is guaranteed that the last character of the first row is always "A", the first character of the last line is always "M". The remaining characters are "." or "S".

Output

If Maria wins, print string "WIN". If the statues win, print string "LOSE".

Examples

Input

.......A
........
........
........
........
........
........
M.......


Output

WIN


Input

.......A
........
........
........
........
........
SS......
M.......


Output

LOSE


Input

.......A
........
........
........
........
.S......
S.......
MS......


Output

LOSE
"""

from collections import defaultdict
from copy import deepcopy

def determine_winner(board):
    def valid(i, j):
        (n, m) = [8] * 2
        return i > -1 and i < n and j > -1 and j < m

    def check(x, y, step):
        if step + 1 < 8 and all_boards[step + 1][x][y] == 'S' or (step < 8 and all_boards[step][x][y] == 'S'):
            return False
        return True

    def dfs(x, y):
        stack, visit, step = [[x, y, -1]], defaultdict(int), -1
        while stack:
            x, y, step = stack.pop()
            step += 1
            if board[x][y] == 'A':
                return 'WIN'
            st = 0
            for i in range(9):
                nx, ny = x + dx[i], y + dy[i]
                if i == 0:
                    if step >= 8:
                        continue
                    else:
                        visit[nx, ny] = 0
                if valid(nx, ny) and check(nx, ny, step) and not visit[nx, ny]:
                    stack.append([nx, ny, step])
                    visit[nx, ny] = 1
                else:
                    st += 1
            if st == 9:
                step -= 1
                visit[x, y] = 0
        return 'LOSE'

    dx, dy = [0, -1, 0, 1, 0, 1, -1, 1, -1], [0, 0, 1, 0, -1, 1, -1, -1, 1]
    all_boards = [board]
    ini = [['.' for _ in range(8)] for _ in range(8)]
    
    for k in range(1, 9):
        tem = deepcopy(ini)
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'S' and i - k > -1:
                    tem[i - k][j] = 'S'
        all_boards.append(tem)
    
    return dfs(0, 0)