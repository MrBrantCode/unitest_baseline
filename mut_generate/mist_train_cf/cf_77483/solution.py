"""
QUESTION:
Write a function `slidingPuzzle` that solves a 2x2 sliding puzzle. The puzzle starts at the given state `grid` and the goal is to reach the final state `[[1,2],[3,0]]`. The function should return the minimum number of moves to reach the final state. If it's impossible to reach the final state, return -1. The puzzle can only move the empty space (0) up, down, left, or right to an adjacent space.
"""

def slidingPuzzle(grid):
    final = [[1,2],[3,0]]
    if grid == final: return 0
    
    def state(g):
        return str(g)
    
    def adjacents(g):
        x, y = 0, 0
        for r in range(2):
            for c in range(2):
                if g[r][c] == 0:
                    x, y = r, c
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 0 <= ny < 2:
                newGrid = [lst[:] for lst in g]
                newGrid[x][y], newGrid[nx][ny] = newGrid[nx][ny], newGrid[x][y]
                yield newGrid
    
    distances = {state(grid): 0}
    queue = [(grid, 0)]
    while queue:
        current, step = queue.pop(0)
        for nextGrid in adjacents(current):
            newState = state(nextGrid)
            if newState not in distances:
                distances[newState] = step + 1
                if nextGrid == final:
                    return distances[state(final)]
                queue.append((nextGrid, step + 1))
    return -1