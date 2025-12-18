"""
QUESTION:
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell 
1 : Cells have fresh oranges 
2 : Cells have rotten oranges 
We have to determine what is the minimum time required to rot all oranges. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
 
Example 1:
Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and 
(2,1) in unit time.
Example 2:
Input: grid = {{2,2,0,1}}
Output: -1
Explanation: The grid is-
2 2 0 1
Oranges at (0,0) and (0,1) can't rot orange at
(0,3).
 
Your Task:
You don't need to read or print anything, Your task is to complete the function orangesRotting() which takes grid as input parameter and returns the minimum time to rot all the fresh oranges. If not possible returns -1.
 
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
 
Constraints:
1 ≤ n, m ≤ 500
"""

def oranges_rotting(grid):
    from collections import deque
    
    q = deque()
    (m, n) = (len(grid), len(grid[0]))
    count_oranges = 0
    
    # Initialize the queue with all rotten oranges and count fresh oranges
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            if grid[i][j] == 1:
                count_oranges += 1
    
    # If there are no fresh oranges, return 0
    if count_oranges == 0:
        return 0
    
    # If there are no rotten oranges, return -1
    if not q:
        return -1
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    minutes = 0
    
    # Perform BFS
    while q:
        size = len(q)
        while size > 0:
            (x, y) = q.popleft()
            size -= 1
            for (dx, dy) in directions:
                (i, j) = (x + dx, y + dy)
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    grid[i][j] = 2
                    count_oranges -= 1
                    q.append((i, j))
        minutes += 1
        if count_oranges == 0:
            return minutes
    
    # If there are still fresh oranges left, return -1
    return -1