"""
QUESTION:
Write a function `isPathPossible(board: List[List[str]]) -> bool` that takes a 2D array of characters representing a game board with 'E' for empty cells and 'O' for obstacles. The function should return `True` if there exists a path from the top-left corner to the bottom-right corner while avoiding obstacles and only moving down or right, and `False` otherwise.
"""

from typing import List

def isPathPossible(board: List[List[str]]) -> bool:
    if not board or not board[0]:
        return False

    rows, cols = len(board), len(board[0])
    dp = [[False] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "O":
                dp[i][j] = False
            elif i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = dp[i][j - 1] and board[i][j] == "E"
            elif j == 0:
                dp[i][j] = dp[i - 1][j] and board[i][j] == "E"
            else:
                dp[i][j] = (dp[i - 1][j] or dp[i][j - 1]) and board[i][j] == "E"

    return dp[rows - 1][cols - 1]