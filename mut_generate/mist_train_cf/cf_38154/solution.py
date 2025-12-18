"""
QUESTION:
Given a 2D list of characters `board` and a string `word`, determine if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are those horizontally or vertically neighboring, and the same letter cell may not be used more than once.

Write a function `exist(board, word)` that takes in the `board` and `word` and returns `True` if the word exists in the grid, and `False` otherwise.
"""

def exist(board, word):
    def dfs(i, j, k):
        if not (0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[k]):
            return False
        if k == len(word) - 1:
            return True
        temp, board[i][j] = board[i][j], '/'
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = temp
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False