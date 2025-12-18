"""
QUESTION:
Given a triangle array, return the minimum path sum to reach from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
Example 1:
Input:
n = 4
triangle = [[2],
           [3,4],
          [6,5,7],
         [4,1,8,3]]
Output:
11
Explanation:
     2
   3 4
  6 5 7
 4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.
Example 2:
Input:
n =  1
triangle = [[10]]
Output:
10
Your Task:
You don't have to read input or print anything. Your task is to complete the function minimizeSum() which takes integer n and the triangle and returns the minimum sum to reach from top to bottom.
Constraint:
1 <= triangle.length <= 200
triangle[i].length =  triangle[i-1].length + 1
1 <= triangle[i][j] <= 1000
Expected Time Complexity: O(n * n)
Expected Space Complexity: O(n* n)
"""

def minimum_path_sum(triangle):
    n = len(triangle)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    
    def cost(i, j):
        if dp[i][j] != -1:
            return dp[i][j]
        if i == n - 1:
            return triangle[i][j]
        down = triangle[i][j] + cost(i + 1, j)
        right = triangle[i][j] + cost(i + 1, j + 1)
        dp[i][j] = min(down, right)
        return dp[i][j]
    
    return cost(0, 0)