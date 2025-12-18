"""
QUESTION:
Design a function `maxPath(matrix, p)` that finds the path with the maximum sum of values, consisting of `p` elements within an MxM matrix, where M >= 3. Each cell of the matrix contains a distinct value from 1 to M*M. The function should start from any cell and move to adjacent cells connected by an edge, returning a sorted list displaying the values along this path in descending order. The function should not include any repeated values in the path and should not move outside the matrix boundaries.
"""

def maxPath(matrix, p):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited, maxPath = set(), []

    def dfs(row, col, p, path):
        nonlocal maxPath
        if p == 0:
            maxPath = max(maxPath, path, key = lambda x: sum(x))
            return
        for i,j in [(0,1), (0,-1), (1,0), (-1,0)]:
            newRow, newCol = row + i, col + j
            if 0 <= newRow < rows and 0 <= newCol < cols and (newRow,newCol) not in visited:
                visited.add((newRow, newCol))
                dfs(newRow, newCol, p - 1, path + [matrix[newRow][newCol]])
                visited.remove((newRow, newCol))

    for i in range(rows):
        for j in range(cols):
            visited.add((i, j))
            dfs(i, j, p - 1, [matrix[i][j]])
            visited.remove((i, j))

    maxPath.sort(reverse=True)
    return maxPath