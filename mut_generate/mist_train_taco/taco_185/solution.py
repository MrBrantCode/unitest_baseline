"""
QUESTION:
Given a matrix A of dimensions NxN where every element is either O or X. Find the largest subsquare surrounded by X.
Example 1:
Input:
N=2
A=[[X,X][X,X]]
Output:
2
Explanation:
The largest square submatrix 
surrounded by X is the whole 
input matrix.
Example 2:
Input:
N=4
A=[[X,X,X,O],[X,O,X,X],
[X,X,X,O],[X,O,X,X]]
Output:
3
Explanation:
Here,the input represents following 
matrix of size 4 x 4
X X X O
X O X X
X X X O
X O X X
The square submatrix starting at 
(0,0) and ending at (2,2) is the 
largest submatrix surrounded by X.
Therefore, size of that matrix would be 3.
Your Task:
You don't need to read input or print anything. Your task is to complete the function largestSubsquare() which takes the integer N and the matrix A as input parameters and returns the size of the largest subsquare surrounded by 'X'.
Expected Time Complexity:O(N^{2})
Expected Auxillary Space:O(N^{2})
Constraints:
1<=N<=1000
A[i][j]={'X','O'}
"""

def largest_subsquare(N, A):
    # Initialize a 3D list to store the counts of 'X' in horizontal and vertical directions
    m = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(2)]
    
    # Fill the horizontal counts
    for i in range(N):
        m[0][i][0] = 1 if A[i][0] == 'X' else 0
        for j in range(1, N):
            if A[i][j] == 'X':
                m[0][i][j] = m[0][i][j - 1] + 1
    
    # Fill the vertical counts
    for j in range(N):
        m[1][0][j] = 1 if A[0][j] == 'X' else 0
        for i in range(1, N):
            if A[i][j] == 'X':
                m[1][i][j] = m[1][i - 1][j] + 1
    
    # Find the largest subsquare surrounded by 'X'
    ans = 0
    for i in range(N):
        for j in range(N):
            d = min(m[0][i][j], m[1][i][j])
            while d > 0:
                if m[0][i - d + 1][j] >= d and m[1][i][j - d + 1] >= d:
                    ans = max(d, ans)
                    break
                d -= 1
    
    return ans