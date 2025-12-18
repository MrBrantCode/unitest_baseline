"""
QUESTION:
Given an `m x n` integer matrix `heights` representing the height of each unit cell in a continent, return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans without passing through any obstacles. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges. Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height. However, there are obstacles in the form of cells with a height of `-1` which water cannot flow through. 

The function name should be `pacificAtlantic` and it should take `heights` as input.
"""

def pacificAtlantic(heights):
    if not heights: 
        return []
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    m, n = len(heights), len(heights[0])
    pacific_visited = [[0 for _ in range(n)] for _ in range(m)]
    atlantic_visited = [[0 for _ in range(n)] for _ in range(m)]

    def dfs(visited, x, y):
        visited[x][y] = 1
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or visited[new_x][new_y] == 1 or heights[new_x][new_y] == -1:
                continue
            if heights[new_x][new_y] < heights[x][y]: 
                continue 
            dfs(visited, new_x, new_y)

    for i in range(m):
        dfs(pacific_visited, i, 0)
        dfs(atlantic_visited, i, n-1)
    for i in range(n):
        dfs(pacific_visited, 0, i)
        dfs(atlantic_visited, m-1, i)

    res = []
    for i in range(m):
        for j in range(n):
            if pacific_visited[i][j] == 1 and atlantic_visited[i][j] == 1:
                res.append([i,j])
    return res