"""
QUESTION:
Given a binary matrix M with R rows and C columns, where each element of the matrix will be 0 or 1. Find the largest square that can be formed with center (i, j) and contains atmost K 1s. There are Q queries, a single query has two integers denoting the centre (i,j) of the square.
 
Example 1:
Input:
R = 4, C = 5
M = {{1, 0, 1, 0, 0} 
     {1, 0, 1, 1, 1} 
     {1, 1, 1, 1, 1} 
     {1, 0, 0, 1, 0}}
K = 9, Q = 1
q_i[] = {1}
q_j[] = {2}
Output:
3
Explanation:
Maximum length square with center
at (1, 2) that can be formed is of
3 length from (0, 1) to (2, 3).
Example 2:
Input:
R = 3, C = 3
M = {{1, 1, 1} 
     {1, 1, 1} 
     {1, 1, 1}}
K = 9, Q = 2
q_i[] = {1, 2}
q_j[] = {1, 2}
Output :
3 1
Your Task:  
You don't need to read input or print anything. Your task is to complete the function largestSquare() which takes 2 integers R, and C followed by a list of lists M denoting the binary matrix and then three integers i,j, and K as input and returns a list of integers denting the largest Square possible for each query.
Expected Time Complexity: O(R*C + Q*log(MIN_DIST)),  where MIN_DIST is the minimum distance of the center from the edges of the matrix where MIN_DIST is the minimum distance of the center from the edges of the matrix.
Expected Auxiliary Space: O(R*C)
Constraints:
1 ≤ R,C ≤ 500
1 ≤ Q ≤ 10^{4}
0 ≤ K ≤ R*C
0 ≤ i < R
0 ≤ j < C
"""

def find_largest_square(M, R, C, K, Q, q_i, q_j):
    # Precompute the prefix sum matrix
    for i in range(1, R):
        M[i][0] += M[i - 1][0]
    for i in range(1, C):
        M[0][i] += M[0][i - 1]
    for i in range(1, R):
        for j in range(1, C):
            M[i][j] = M[i - 1][j] + M[i][j - 1] - M[i - 1][j - 1] + M[i][j]
    
    res = [0] * Q
    
    # Process each query
    for k in range(Q):
        i = q_i[k]
        j = q_j[k]
        p = 0
        while p + i < R and p + j < C and (i - p >= 0) and (j - p >= 0):
            (a, b, c) = (0, 0, 0)
            if j - p - 1 >= 0:
                a = M[i + p][j - p - 1]
            if i - p - 1 >= 0:
                b = M[i - p - 1][j + p]
            if j - p - 1 >= 0 and i - p - 1 >= 0:
                c = M[i - p - 1][j - p - 1]
            ans = M[i + p][j + p] - a - b + c
            if ans > K:
                break
            else:
                res[k] = 2 * p + 1
            p += 1
    
    return res