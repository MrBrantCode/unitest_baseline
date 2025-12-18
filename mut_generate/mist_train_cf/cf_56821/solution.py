"""
QUESTION:
Write a function `isPrintable` that takes a 2D list `initialGrid` and a 2D list `targetGrid` as input, where `initialGrid` and `targetGrid` have the same dimensions. Return `True` if it is possible to print `targetGrid` from `initialGrid` following the rules of the strange printer, and `False` otherwise. The rules of the strange printer are: 
- On each turn, the printer will print a solid rectangular pattern of a single color on the grid. 
- Once the printer has used a color for the above operation, the same color cannot be used again. 
- The initialGrid is there just to create additional dependencies to be considered. Any color that is initially on the grid must be printed after the colors that are intended to be printed on those cells in the final output (targetGrid).
"""

def isPrintable(initialGrid, targetGrid):
    m, n = len(targetGrid), len(targetGrid[0])
    colors = set()
    for i in range(m):
        for j in range(n):
            colors.add(targetGrid[i][j])
            if initialGrid[i][j] != targetGrid[i][j]:
                colors.add(initialGrid[i][j])

    graph = {color: [] for color in colors}
    visited = {color: False for color in colors}
    onStack = {color: False for color in colors}

    for i in range(m):
        for j in range(n):
            color = targetGrid[i][j]
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and targetGrid[x][y] != color and (initialGrid[x][y] != targetGrid[x][y] or initialGrid[i][j] != targetGrid[i][j]):
                    graph[targetGrid[x][y]].append(color)

    def dfs(node):
        visited[node] = True
        onStack[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if not dfs(neighbor):
                    return False
            elif onStack[neighbor]:
                return False
        onStack[node] = False
        return True

    for color in colors:
        if not visited[color]:
            if not dfs(color):
                return False

    return True