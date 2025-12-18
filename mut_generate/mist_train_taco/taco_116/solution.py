"""
QUESTION:
For a given 2D Matrix before, the corresponding cell (x, y) of the after matrix is calculated as follows: 
res = 0;
for(i = 0; i <= x; i++){
    for( j = 0; j <= y; j++){              
        res += before(i,j);
    }
}
after(x,y) = res;
 
Given an N*M 2D-Matrix after, your task is to find the corresponding before matrix for the given matrix.
 
Example 1:
Input:
N = 2, M = 3
after[][] = {{1, 3, 6},
            {3, 7, 11}}
Output:
1 2 3
2 2 1
Explanation:
The before matrix for the given after matrix
matrix is {{1, 2, 3}, {2, 2, 1}}.
Reason:
According to the code given in problem,
after(0,0) = before(0,0) = 1
after(0,1) = before(0,0) + before(0,1)
= 1 + 2 = 3.
after(0, 2) = before(0,0) + before(0, 1)
+ before(0, 2) = 1 + 2 + 3 = 6.
Similarly we can calculate values for every
cell of the after matrix.
 
Example 2:
Input: 
N = 1, M = 3
after[][] = {{1, 3, 5}}
Output:
1 2 2
Explanation: 
The before matrix for the given after matrix
is {{1, 2, 2}}.
Your Task:
Complete the function computeBeforeMatrix() which takes the integers N, M, and the 2D Matrix after as the input parameters, and returns the before matrix of the given after matrix.
Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N, M, after[i][j]  ≤  10^{9}
"""

def compute_before_matrix(N, M, after):
    # Initialize the before matrix with zeros
    before = [[0 for _ in range(M)] for _ in range(N)]
    
    # Set the value for the first cell
    before[0][0] = after[0][0]
    
    # Calculate the values for the first row
    for i in range(1, M):
        before[0][i] = after[0][i] - after[0][i - 1]
    
    # Calculate the values for the first column
    for i in range(1, N):
        before[i][0] = after[i][0] - after[i - 1][0]
    
    # Calculate the values for the rest of the matrix
    for i in range(1, N):
        for j in range(1, M):
            before[i][j] = after[i][j] - after[i - 1][j] - after[i][j - 1] + after[i - 1][j - 1]
    
    return before