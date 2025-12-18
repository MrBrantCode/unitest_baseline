"""
QUESTION:
Implement the function `play_game(n, obstacles, treasures)` to determine whether a player can navigate from the top-left corner (0, 0) to the bottom-right corner (n-1, n-1) of a grid of size n x n without encountering any obstacles. The player can move up, down, left, or right within the grid and can only visit each position once. 

The function takes in the following parameters:
- `n`: an integer representing the side length of the square grid.
- `obstacles`: a list of tuples representing the positions of obstacles in the grid. Each tuple contains the (x, y) coordinates of an obstacle.
- `treasures`: a list of tuples representing the positions of treasures in the grid. Each tuple contains the (x, y) coordinates of a treasure.

The function should return a boolean value indicating whether the player can win the game.
"""

def play_game(n, obstacles, treasures):
    grid = [[0] * n for _ in range(n)]
    for x, y in obstacles:
        grid[y][x] = -1  # Mark obstacle positions as -1
    for x, y in treasures:
        grid[y][x] = 1  # Mark treasure positions as 1

    def is_valid_move(x, y):
        return 0 <= x < n and 0 <= y < n and grid[y][x] != -1

    def dfs(x, y):
        if x == n - 1 and y == n - 1:
            return True  # Reached the end
        if grid[y][x] == 1:
            return False  # Encountered a treasure
        if grid[y][x] == -1:
            return False  # Encountered an obstacle
        grid[y][x] = -1  # Mark current position as visited
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y) and dfs(new_x, new_y):
                return True
        return False

    return dfs(0, 0)