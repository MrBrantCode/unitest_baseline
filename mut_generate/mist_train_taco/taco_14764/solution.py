"""
QUESTION:
Jeny love Sweets so much. Now she is at famous restaurant and wants to eat M pieces of a particular sweet. Cost of nth sweet can only be determined by the determinant of matrix of order n x n, where n = 1 to M. The (i, j)th term of matrix is given as: A[i][j]= minimum(i, j) *(-1)^{((i-1)*n + (j-1))}.
Matrix indexes starts with 1. The task is to find the cost of M sweets.
Example 1:
Input: M = 1
Output: 1 
Explanation: Matrix of 1*1 is: |1|.
Determinant of matrix 1x1 = 1.
Cost of 1 sweet = 1.
Example 2:
Input: M = 2
Output: 0
Explanation: Matrix of 2*2 is:  |1 -1|
                                |1 -2|.
Determinant of matrix 2x2= -1.
Cost of 2 sweets  = 
Cost of 1st sweet + Cost of 2nd sweet = 1 + -1 = 0.
Your Task:  
You dont need to read input or print anything. Complete the function costOfSweets() which takes M as input parameter and returns the cost of M sweets.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= M <=10^{6}
"""

def calculate_cost_of_sweets(M: int) -> int:
    return M - (M + 2) // 4 * 2