"""
QUESTION:
Implement a function `simulate(board, k)` where `board` is an `m x n` grid of cells representing the current state of the game, and `k` is the number of generations to simulate. The function should return the state of the board after `k` generations, following the rules of Conway's Game of Life with obstacles (represented by -1), live cells (represented by 1), and dead cells (represented by 0).

The board's state should be updated simultaneously according to the rules:

* Any live cell with fewer than two live neighbors dies.
* Any live cell with two or three live neighbors lives.
* Any live cell with more than three live neighbors dies.
* Any dead cell with exactly three live neighbors becomes a live cell.
* Obstacles do not interact with the cells and remain unchanged.

Constraints: `m == board.length`, `n == board[i].length`, `1 <= m, n <= 50`, `board[i][j]` is `0`, `1`, or `-1`, and `1 <= k <= 100`. The function should be able to handle the simulation in-place without using extra space proportional to the size of the input.
"""

import copy

def gameOfLife(board, k):
    m, n = len(board), len(board[0])
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1],[0, 1], [1, -1], [1, 0], [1, 1]]

    for _ in range(k):

        new_board = copy.deepcopy(board)

        for i in range(m):
            for j in range(n):
                
                if board[i][j] == -1:
                    continue
                
                live_neighbors = 0

                for dir in dirs:
                    ni, nj = i + dir[0], j + dir[1]
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 1:
                        live_neighbors += 1

                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    new_board[i][j] = 0
                elif board[i][j] == 0 and live_neighbors == 3:
                    new_board[i][j] = 1

        board = new_board
    
    return board