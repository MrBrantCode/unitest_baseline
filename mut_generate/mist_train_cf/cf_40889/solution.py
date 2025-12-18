"""
QUESTION:
Implement the `exist` function, which takes a 2D list of lowercase English letters (`board`) and a word as input. The function should return `True` if the word can be constructed from sequentially adjacent cells in the board (horizontally or vertically neighboring) without using the same letter cell more than once, and `False` otherwise.
"""

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    def dfs(i: int, j: int, k: int) -> bool:
        if not (0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[k]):
            return False
        if k == len(word) - 1:
            return True
        temp, board[i][j] = board[i][j], '/'
        found = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = temp
        return found

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False