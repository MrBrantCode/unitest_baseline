"""
QUESTION:
Implement the function `explore_abyss(abyss)` that takes a 2D list of characters `abyss` and returns a boolean value indicating whether the player can successfully navigate from 'S' to 'E' by moving through '.' while avoiding '#'. The grid can be traversed in four directions: up, down, left, and right. The function should only consider the input grid and return True if a path exists, False otherwise.
"""

def explore_abyss(abyss):
    rows, cols = len(abyss), len(abyss[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols and abyss[row][col] != '#'

    def dfs(row, col):
        if not is_valid_move(row, col):
            return False
        if abyss[row][col] == 'E':
            return True
        abyss[row][col] = '#'  # Mark the cell as visited
        for dr, dc in directions:
            if dfs(row + dr, col + dc):
                return True
        return False

    for i in range(rows):
        for j in range(cols):
            if abyss[i][j] == 'S':
                return dfs(i, j)

    return False