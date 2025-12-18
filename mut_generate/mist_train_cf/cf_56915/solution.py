"""
QUESTION:
Write a function named `bishopChess(N, K, r, c)` that takes four parameters: `N` (the dimension of the chessboard, ranging from 1 to 25), `K` (the number of moves, ranging from 0 to 100), `r` (the starting row of the bishop, 0-indexed), and `c` (the starting column of the bishop, 0-indexed). The function should calculate and return the probability that the bishop remains on the board after it has stopped moving.
"""

def bishopChess(N, K, r, c):
    dp_prev = [[0 for _ in range(N)] for _ in range(N)]
    dp_prev[r][c] = 1
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 

    for _ in range(K):
        dp = [[0 for _ in range(N)] for _ in range(N)] 
        for i in range(N):
            for j in range(N):
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < N:
                        dp[i][j] += dp_prev[ni][nj]/4
        dp_prev = dp
        
    return sum(sum(dp_prev, []))