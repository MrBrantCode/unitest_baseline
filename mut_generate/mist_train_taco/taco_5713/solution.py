"""
QUESTION:
Given a matrix mat of size R*C with 0 and 1s, find the largest rectangle of all 1s in the matrix. The rectangle can be formed by swapping any pair of columns of given matrix.
Example 1:
Input: 
R = 3, C = 5
mat[][] = {{0, 1, 0, 1, 0},
           {0, 1, 0, 1, 1},
           {1, 1, 0, 1, 0}};
Output: 6
Explanation: The largest rectangle's area
is 6. The rectangle can be formed by
swapping column  2 with 3. The matrix
after swapping will be
     0 0 1 1 0
     0 0 1 1 1
     1 0 1 1 0
Example 2:
Input:
R = 4, C = 5
mat[][] = {{0, 1, 0, 1, 0},
           {0, 1, 1, 1, 1},
           {1, 1, 1, 0, 1},
           {1, 1, 1, 1, 1}};
Output: 9
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxArea() which takes the 2D array of booleans mat, r and c as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(R*(R + C))
Expected Auxiliary Space: O(R*C)
Constraints:
1<= R,C <=10^{3}
0 <= mat[i][j] <= 1
"""

def max_rectangle_area(mat, r, c):
    # Initialize a histogram matrix to store the heights of the bars
    hist = [[0 for _ in range(c)] for _ in range(r)]
    
    # Fill the histogram matrix
    for j in range(c):
        hist[0][j] = mat[0][j]
    for i in range(1, r):
        for j in range(c):
            if mat[i][j]:
                hist[i][j] = hist[i - 1][j] + mat[i][j]
    
    # Sort each row of the histogram matrix in descending order
    for i in range(r):
        hist[i].sort(reverse=True)
    
    # Calculate the maximum area of the rectangle
    ans = 0
    for i in range(r):
        for j in range(c):
            ans = max(ans, hist[i][j] * (j + 1))
    
    return ans