"""
QUESTION:
You have got a maze, which is a n*n Grid. Every cell of the maze contains these numbers 1, 2 or 3. 
If it contains 1 : means we can go Right from that cell only.
If it contains 2 : means we can go Down from that cell only.
If it contains 3 : means we can go Right and Down to both paths from that cell.
We cant go out of the maze at any time.
Initially, You are on the Top Left Corner of The maze(Entry). And, You need to go to the Bottom Right Corner of the Maze(Exit).
You need to find the total number of paths from Entry to Exit Point.
There may be many paths but you need to select that path which contains the maximum number of Adventure.
The Adventure on a path is calculated by taking the sum of all the cell values thatlies in the path.
 
Example 1:
Input: matrix = {{1,1,3,2,1},{3,2,2,1,2},
{1,3,3,1,3},{1,2,3,1,2},{1,1,1,3,1}}
Output: {4,18}
Explanation: There are total 4 Paths Available 
out of which The Max Adventure is 18. Total 
possible Adventures are 18,17,17,16. Of these 
18 is the maximum.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function FindWays() which takes matrix as input parameter and returns a list containg total number of ways to reach at (n, n) modulo 10^{9} + 7 and maximum number of Adventure.
 
Expected Time Complexity: O(n^{2})
Expected Space Complexity: O(n^{2})
 
Constraints:
1 <= n <= 100
"""

def find_ways_in_maze(matrix):
    m = len(matrix[0])
    n = len(matrix)
    dp = [[[-1, 0] for _ in range(m)] for _ in range(n)]
    dp[0][0][0] = 1
    dp[0][0][1] = matrix[0][0]
    
    for i in range(1, m):
        if (matrix[0][i - 1] == 1 or matrix[0][i - 1] == 3) and dp[0][i - 1][0] != -1:
            dp[0][i][0] = dp[0][i - 1][0]
            dp[0][i][1] = dp[0][i - 1][1] + matrix[0][i]
    
    for j in range(1, n):
        if (matrix[j - 1][0] == 2 or matrix[j - 1][0] == 3) and dp[j - 1][0][0] != -1:
            dp[j][0][0] = dp[j - 1][0][0]
            dp[j][0][1] = dp[j - 1][0][1] + matrix[j][0]
    
    for i in range(1, n):
        for j in range(1, m):
            if (matrix[i - 1][j] == 2 or matrix[i - 1][j] == 3) and dp[i - 1][j][0] != -1:
                dp[i][j][0] = dp[i - 1][j][0]
                dp[i][j][1] = dp[i - 1][j][1] + matrix[i][j]
            if (matrix[i][j - 1] == 1 or matrix[i][j - 1] == 3) and dp[i][j - 1][0] != -1:
                dp[i][j][0] = max(dp[i][j][0], 0)
                dp[i][j][0] += dp[i][j - 1][0]
                dp[i][j][1] = max(dp[i][j][1], dp[i][j - 1][1] + matrix[i][j])
    
    dp[n - 1][m - 1][0] = max(dp[n - 1][m - 1][0], 0)
    dp[n - 1][m - 1][0] = dp[n - 1][m - 1][0] % (10**9 + 7)
    
    return dp[n - 1][m - 1]