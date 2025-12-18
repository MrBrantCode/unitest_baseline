"""
QUESTION:
Implement the `navigate_maze` function that takes a 2D list `maze`, a `start` position as a tuple (x, y), and `dimensions` as a tuple (rows, columns). The function should return True if the character can reach the exit 'E' from the start position without stepping on a trap 'T', and False otherwise. The character can move up, down, left, or right within the maze, but cannot move through walls '#' or traps 'T'. The maze is 0-indexed and the start position is also 0-indexed.
"""

def navigate_maze(maze, start, dimensions):
    def is_valid_move(x, y):
        return 0 <= x < dimensions[0] and 0 <= y < dimensions[1] and maze[x][y] != '#'

    def dfs(x, y):
        if not is_valid_move(x, y):
            return False
        if maze[x][y] == 'E':
            return True
        if maze[x][y] == 'T':
            return False

        maze[x][y] = '#'  # Mark current cell as visited

        # Explore all possible directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            if dfs(x + dx, y + dy):
                return True

        return False

    return dfs(start[0], start[1])