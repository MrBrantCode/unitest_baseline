"""
QUESTION:
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Example 1:
heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explaination: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Your Task:
You don't need to read input or print anything. Your task is to complete the function MinimumEffort() which takes the array height  and Returns the minimum effort required to travel from the top-left cell to the bottom-right cell.
Constraints
rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 10^{6}
 
Expected Time Complexity: O(Elog(V))
Expected Space Complexity: O(N,M)
"""

import heapq

def minimum_effort_path(heights):
    row = len(heights)
    col = len(heights[0])
    dis = [[float('inf')] * col for _ in range(row)]
    dis[0][0] = 0
    row_dir = [-1, 0, 1, 0]
    col_dir = [0, -1, 0, 1]
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    
    while heap:
        cur_dis, cur_row, cur_col = heapq.heappop(heap)
        
        for d in range(4):
            x = cur_row + row_dir[d]
            y = cur_col + col_dir[d]
            
            if 0 <= x < row and 0 <= y < col:
                new_wt = max(abs(heights[cur_row][cur_col] - heights[x][y]), cur_dis)
                
                if new_wt < dis[x][y]:
                    dis[x][y] = new_wt
                    heapq.heappush(heap, [new_wt, x, y])
    
    return dis[-1][-1]