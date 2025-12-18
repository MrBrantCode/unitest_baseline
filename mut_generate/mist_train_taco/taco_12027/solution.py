"""
QUESTION:
Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.
Example 1:
Input:
R=4
C=5
M=[[1,2,-1,-4,-20],
[-8,-3,4,2,1],
[3,8,10,1,3],
[-4,-1,1,7,-6]]
Output:
29
Explanation:
The matrix is as follows and the
blue rectangle denotes the maximum sum
rectangle.
Example 2:
Input:
R=2
C=2
M=[[-1,-2],[-3,-4]]
Output:
-1
Explanation:
Taking only the first cell is the 
optimal choice.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maximumSumRectangle() which takes the number R, C, and the 2D matrix M as input parameters and returns the maximum sum submatrix.
Expected Time Complexity:O(R*R*C)
Expected Auxillary Space:O(R*C)
 
Constraints:
1<=R,C<=500
-1000<=M[i][j]<=1000
"""

def maximum_sum_rectangle(R, C, M):
    pre = [[0] * (C + 1) for _ in range(R)]
    ans = -1000000000000000
    
    for i in range(R):
        for j in range(C):
            pre[i][j + 1] += pre[i][j] + M[i][j]
            ans = max(ans, M[i][j])
    
    for i in range(C):
        for j in range(i, C):
            sy, ey = i, j + 1
            ca = -1000000000000000
            mtt = -1000000000000000
            for k in range(R):
                cv = pre[k][ey] - pre[k][sy]
                mtt = max(cv, cv + mtt)
                ca = max(ca, mtt)
            ans = max(ans, ca)
    
    return ans