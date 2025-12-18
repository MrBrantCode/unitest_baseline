"""
QUESTION:
Implement the `play_game(grid)` function that takes a 2D array `grid` as input and returns the maximum possible score the player can achieve by navigating through the grid. The grid is represented as a list of lists where each cell can contain one of the following symbols: '.' (empty space), 'X' (obstacle), 'T' (treasure), and 'E' (exit point). The player starts at the top-left corner and can move in four directions: up, down, left, and right. If the exit point is unreachable, return -1.
"""

def play_game(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] != 'X'

    def dfs(row, col, score):
        if not is_valid_move(row, col):
            return -1
        if grid[row][col] == 'E':
            return score
        if grid[row][col] == 'T':
            score += 1
        max_score = -1
        temp = grid[row][col]
        grid[row][col] = 'X'  # Mark current cell as visited
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_score = dfs(new_row, new_col, score)
            if new_score > max_score:
                max_score = new_score
        grid[row][col] = temp  # Revert the cell back to its original state
        return max_score

    return dfs(0, 0, 0)