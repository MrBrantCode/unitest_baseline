"""
QUESTION:
Given an N x M matrix, with a few hurdles(denoted by 0) arbitrarily placed, calculate the length of the longest possible route possible from source(xs,ys) to a destination(xd,yd) within the matrix. We are allowed to move to only adjacent cells which are not hurdles. The route cannot contain any diagonal moves and a location once visited in a particular path cannot be visited again.If it is impossible to reach the destination from the source return -1.
 
Example 1:
Input:
{xs,ys} = {0,0}
{xd,yd} = {1,7}
matrix = 1 1 1 1 1 1 1 1 1 1
         1 1 0 1 1 0 1 1 0 1
         1 1 1 1 1 1 1 1 1 1
Output: 24
Explanation:
 
Example 2:
Input: 
{xs,ys} = {0,3}
{xd,yd} = {2,2}
matrix = 1 0 0 1 0
         0 0 0 1 0
         0 1 1 0 0
Output: -1
Explanation:
We can see that it is impossible to
reach the cell (2,2) from (0,3).
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestPath() which takes matrix ,source and destination as input parameters and returns an integer denoting the longest path.
Expected Time Complexity: O(2^(N*M))
Expected Auxiliary Space: O(N*M)
Constraints:
1 <= N,M <= 10
"""

def longest_path(matrix, source, destination):
    n = len(matrix)
    m = len(matrix[0])
    xs, ys = source
    xd, yd = destination
    ans = -1
    dir_x = [0, 0, 1, -1]
    dir_y = [1, -1, 0, 0]

    def isvalid(mat, n, m, xs, ys):
        if xs < 0 or ys < 0:
            return False
        if xs >= n or ys >= m:
            return False
        if mat[xs][ys] != 1:
            return False
        return True

    def solve(mat, n, m, xs, ys, xd, yd, dist):
        nonlocal ans
        if xs == xd and ys == yd:
            ans = max(ans, dist)
            return
        for i in range(4):
            dist += 1
            mat[xs][ys] = -1
            xs += dir_x[i]
            ys += dir_y[i]
            if isvalid(mat, n, m, xs, ys):
                solve(mat, n, m, xs, ys, xd, yd, dist)
            xs -= dir_x[i]
            ys -= dir_y[i]
            mat[xs][ys] = 1
            dist -= 1

    if matrix[xs][ys] != 1:
        return -1
    solve(matrix, n, m, xs, ys, xd, yd, 0)
    return ans