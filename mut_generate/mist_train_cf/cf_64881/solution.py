"""
QUESTION:
Write a function `findWords` that takes a 2D list `board` and a list of strings `words` as input, and returns a list of all words in `words` that can be formed by connecting adjacent cells (horizontally or vertically) in `board` that contain the corresponding letters. Each cell can only be used once in each word. The function should return the words in the order they appear in `words`. The function should also have a helper function `dfs` to perform a depth-first search on the board.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def findWords(board, words):
    root = TrieNode()
    for word in words:
        node = root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = word

    result = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in root.children:
                dfs(board, i, j, root.children[board[i][j]], result)
    return result

def dfs(board, i, j, node, result):
    if node.word:
        result.append(node.word)
        node.word = None
    temp, board[i][j] = board[i][j], '/'
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = i + x, j + y
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] in node.children:
            dfs(board, nx, ny, node.children[board[nx][ny]], result)
    board[i][j] = temp
    if not node.children:
        del node