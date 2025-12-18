"""
QUESTION:
Write a function `slidingPuzzle(grid)` that takes a 2x2 grid as input where `grid[i][j]` is a permutation of `[0, 1, 2, 3]`. The function should return the least number of moves required to transform the grid into `[[1,2],[3,0]]` by swapping the empty square (0) with a diagonally adjacent number. If it is impossible to transform the grid into the target state, return -1.
"""

def slidingPuzzle(grid):
    final = [[1,2],[3,0]]
    if grid == final: 
        return 0
    
    def state(grid):
        return str(grid)

    def adjacents(grid):
        x, y = 0, 0
        for r in range(2):
            for c in range(2):
                if grid[r][c] == 0:
                    x, y = r, c
        for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 0 <= ny < 2:
                newGrid = [lst[:] for lst in grid]
                newGrid[x][y], newGrid[nx][ny] = newGrid[nx][ny], newGrid[x][y]
                yield newGrid

    distances = {state(grid): 0}
    queue = [[grid, 0]]
    
    while queue:
        current, step = queue.pop(0)
        for nextGrid in adjacents(current):
            newState = state(nextGrid)
            if newState not in distances:
                distances[newState] = step + 1
                if newState == str(final):
                    return distances[newState]
                queue.append([nextGrid, step + 1])
    return -1