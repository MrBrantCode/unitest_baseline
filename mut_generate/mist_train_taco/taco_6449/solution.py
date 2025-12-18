"""
QUESTION:
Write a function that determines whether a string is a valid guess in a Boggle board, as per the rules of Boggle. A Boggle board is a 2D array of individual characters, e.g.:
```python
[ ["I","L","A","W"],
  ["B","N","G","E"],
  ["I","U","A","O"],
  ["A","S","R","L"] ]
```
Valid guesses are strings which can be formed by connecting adjacent cells (horizontally, vertically, or diagonally) without re-using any previously used cells.

For example, in the above board "BINGO", "LINGO", and "ILNBIA" would all be valid guesses, while "BUNGIE", "BINS", and "SINUS" would not.

Your function should take two arguments (a 2D array and a string) and return true or false depending on whether the string is found in the array as per Boggle rules.

Test cases will provide various array and string sizes (squared arrays up to 150x150 and strings up to 150 uppercase letters). You do not have to check whether the string is a real word or not, only if it's a valid guess.
"""

def is_valid_boggle_guess(board, word):
    # Extend the board with an extra row and column of empty strings to simplify boundary checks
    grid = [list(row) + [''] for row in board] + [[''] * (len(board[0]) + 1)]
    
    def dfs(x, y, i):
        # If we've matched the entire word, return True
        if i == len(word):
            return True
        # If the current cell doesn't match the current character of the word, return False
        if grid[x][y] != word[i]:
            return False
        # Temporarily mark the current cell as visited by setting it to an empty string
        grid[x][y] = ''
        # Recursively check all 8 possible directions (horizontally, vertically, diagonally)
        result = any(dfs(x + dx, y + dy, i + 1) for dx in range(-1, 2) for dy in range(-1, 2) if dx != 0 or dy != 0)
        # Restore the original value of the cell
        grid[x][y] = word[i]
        return result
    
    # Start the search from every cell in the board
    return any(dfs(x, y, 0) for x in range(len(board)) for y in range(len(board[0])))