"""
QUESTION:
Create a method named maxSumPath that takes a 2D grid of size NxN (where N is at least 3) and an integer k (where k ≤ N*N) as inputs. The grid contains unique values from 1 to N*N in each cell. The function should find the maximum sum of exactly k non-repeating cells in the grid, considering movements only to adjacent cells (up, down, left, or right) from the current cell. The function should return the sequence of the maximum sum path.
"""

def maxSumPath(grid, k):
    n = len(grid)
    m = len(grid[0])
    max_sum_path = [[grid[0][0]]]

    def is_valid(cell, visited_cells):
        x, y = cell
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
            return False
        if cell in visited_cells:
            return False
        return True

    def dfs(cell, steps_left, visited_cells, path):
        if steps_left == 0:
            sum_path = sum(path)
            if sum_path > sum(max_sum_path[0]):
                max_sum_path[0] = path.copy()
            return

        x , y = cell
        for dx, dy in [(-1,0), (1,0), (0, -1), (0, 1)]:
            next_cell = (x+dx, y+dy)
            if is_valid(next_cell, visited_cells):
                visited_cells.add(next_cell)
                path.append(grid[next_cell[0]][next_cell[1]])
                dfs(next_cell, steps_left-1, visited_cells, path)
                path.pop()
                visited_cells.remove(next_cell)

    for i in range(n):
        for j in range(m):
            visited_cells = {(i, j)}
            path = [grid[i][j]]
            dfs((i, j), k-1, visited_cells, path)

    return max_sum_path[0]