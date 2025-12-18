"""
QUESTION:
Write a function `exist(board, word)` that returns true if the word exists in the grid and false otherwise. The function takes two parameters: `board` (a 2D grid of characters) and `word` (a string). The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally, vertically or diagonally neighboring. The same letter cell may not be used more than once. The function has the following constraints: `m == board.length`, `n = board[i].length`, `1 <= m, n <= 6`, `1 <= word.length <= 15`, and `board` and `word` consist of only lowercase and uppercase English letters.
"""

def exist(board, word):
    def dfs(ind, i, j, board, word):
        if board[i][j] != word[ind]:
            return False
        if ind == len(word) - 1:
            return True

        tmp, board[i][j] = board[i][j], '/'
        res = any(dfs(ind + 1, i + x, j + y, board, word) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)] if 0 <= i + x < len(board) and 0 <= j + y < len(board[0]))
        board[i][j] = tmp
        return res
      
    m, n = len(board), len(board[0])
    return any(dfs(0, i, j, board, word) for i in range(m) for j in range(n))