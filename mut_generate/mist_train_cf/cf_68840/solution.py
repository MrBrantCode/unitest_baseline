"""
QUESTION:
Create a function maxSumPath that finds the highest cumulative sum of precisely k cells from a square matrix of NxN dimensions, where each cell holds a unique value ranging from 1 to N*N. The traversal can begin from any cell but can only proceed to directly adjoining cells. The function should return the maximum cumulative path sum as an integer. 

Restrictions: 
- The input grid is a square matrix of NxN dimensions.
- Each cell in the grid holds a unique value ranging from 1 to N*N.
- The traversal can only proceed to directly adjoining cells.
- The function should handle exceptions and produce the maximum cumulative path value.
"""

def maxSumPath(grid, k):
    import heapq  
    n = len(grid)
    paths = [[-1]*n for _ in range(n)]  

    heap = [(-grid[0][0], 1, 0, 0)] 
    while heap:
        sum_so_far, steps, y, x = heapq.heappop(heap)  
        if steps > paths[y][x]:  
            paths[y][x] = steps
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
                newx, newy = x + dx, y + dy 
                if 0 <= newx < n and 0 <= newy < n and steps < k:  
                    heapq.heappush(heap, (sum_so_far - grid[newy][newx], steps + 1, newy, newx))

    return max(map(max, paths))*-1