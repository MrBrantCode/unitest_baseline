"""
QUESTION:
Implement the `navigate_maze(maze)` function, which takes a 2D list `maze` as input and returns a boolean value indicating whether it is possible to navigate from the top-left corner to the bottom-right corner without encountering any obstacles. The maze is represented as a 2D list of integers where 0 represents an open path and 1 represents a wall or obstacle.
"""

def entrance(maze):
    def is_valid_move(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

    def dfs(x, y):
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            return True
        if is_valid_move(x, y):
            maze[x][y] = -1  # Mark as visited
            if dfs(x + 1, y) or dfs(x, y + 1) or dfs(x - 1, y) or dfs(x, y - 1):
                return True
        return False

    return dfs(0, 0)