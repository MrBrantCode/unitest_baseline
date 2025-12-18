"""
QUESTION:
You are given a matrix having n rows and m columns. The special property of this matrix is that some of the cells of this matrix are given as input, which are blocked i.e. they cannot be reached. Now you have to start from the cell (1,1) and reach the end (n,m) provided during the journey you can move horizontally right from the current cell or vertically down from the current cell. Can you answer the number of ways you can traverse the matrix obeying the above constraints starting from (1,1) and ending at (n,m).
 
Example 1:
Input: n = 3, m = 3, k = 2,
blocked_cells = {{1,2},{3,2}}.
Output: 1
Explanation: There is only one path from
(1,1) to(3,3) which is (1,1)->(2,1)->(2,2)->
(2,3)->(3,3).
Example 2:
Input: n = 5, m = 5, k = 1,
blocked_cells = {{5,5}}
Output: 0
Explanation: There is no path to reach at 
(5,5) beacuse (5,5) is blocked.
 
Your Task:
You don't need to read or print anything, Your task is to complete the function FindWays() which takes n, m and blocked_cells as input parameter and returns total number of ways to reach at (n, m) modulo 10^{9} + 7.
 
Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)
 
Constraints:
1 <= n, m <= 500
1 <= k <= n*m
"""

def find_ways(n, m, blocked_cells):
    # Initialize the grid with 1s, meaning all cells are initially reachable
    grid = [[1] * m for _ in range(n)]
    
    # Mark the blocked cells as 0 (unreachable)
    for (i, j) in blocked_cells:
        grid[i - 1][j - 1] = 0
    
    # Update the first column based on blocked cells
    for i in range(1, n):
        grid[i][0] &= grid[i - 1][0]
    
    # Update the first row based on blocked cells
    for j in range(1, m):
        grid[0][j] &= grid[0][j - 1]
    
    # Calculate the number of ways to reach each cell
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j]:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    
    # Return the number of ways to reach the bottom-right cell modulo 10^9 + 7
    return grid[n - 1][m - 1] % (10 ** 9 + 7)