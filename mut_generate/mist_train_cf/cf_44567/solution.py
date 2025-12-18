"""
QUESTION:
Write a function `shortest_path` that takes as input a 2D list `board` representing the nxm board, and an integer `target` representing the target value. The function should return the shortest path from the top left cell to the bottom right cell such that the sum of the values of the cells visited on the path is equal to `target`. The path must not cross itself and must not visit any cell more than once. If no such path exists, return "No Solution". The path can move in four directions: up, down, left, and right. Note that the function should use a heuristic approach and may not always guarantee the optimal solution.
"""

import heapq

def shortest_path(board, target):
    n, m = len(board), len(board[0])
    if board[0][0] > target or board[n-1][m-1] > target:
        return "No Solution"
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pq = [(board[0][0], 0, 0, [(0, 0)])]
    visited = set((0, 0))
    
    while pq:
        curr_sum, x, y, path = heapq.heappop(pq)
        if curr_sum > target:
            continue
        if x == n - 1 and y == m - 1 and curr_sum == target:
            return path
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < m) and (nx, ny) not in visited:
                if board[nx][ny] > target - curr_sum:
                    continue
                new_sum = curr_sum + board[nx][ny]
                new_path = path + [(nx, ny)]
                new_cost = new_sum + abs(nx - (n - 1)) + abs(ny - (m - 1))
                heapq.heappush(pq, (new_sum, nx, ny, new_path))
                visited.add((nx, ny))
                
    return "No Solution"