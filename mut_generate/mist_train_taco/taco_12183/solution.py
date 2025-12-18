"""
QUESTION:
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:


Input:
11110
11010
11000
00000

Output: 1


Example 2:


Input:
11000
11000
00100
00011

Output: 3
"""

def count_islands(grid):
    def expand_island(i, j):
        edges = [(i, j)]
        while edges:
            next_edges = []
            for edge in edges:
                (ei, ej) = edge
                if 0 <= ei < len(grid) and 0 <= ej < len(grid[ei]) and grid[ei][ej] == '1':
                    grid[ei][ej] = '2'
                    next_edges.append((ei + 1, ej))
                    next_edges.append((ei, ej + 1))
                    next_edges.append((ei - 1, ej))
                    next_edges.append((ei, ej - 1))
            edges = next_edges

    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                island_count += 1
                expand_island(i, j)
    return island_count