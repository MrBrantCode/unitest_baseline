"""
QUESTION:
Given a matrix of size r*c. Traverse the matrix in spiral form.
Example 1:
Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Explanation:
Example 2:
Input:
r = 3, c = 4  
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12}}
Output: 
1 2 3 4 8 12 11 10 9 5 6 7
Explanation:
Applying same technique as shown above, 
output for the 2nd testcase will be 
1 2 3 4 8 12 11 10 9 5 6 7.
Your Task:
You dont need to read input or print anything. Complete the function spirallyTraverse() that takes matrix, r and c as input parameters and returns a list of integers denoting the spiral traversal of matrix. 
Expected Time Complexity: O(r*c)
Expected Auxiliary Space: O(r*c), for returning the answer only.
Constraints:
1 <= r, c <= 100
0 <= matrix_{i} <= 100
"""

def spirally_traverse(matrix, r, c):
    res = []
    left = 0
    right = c
    top = 0
    bottom = r
    
    while left < right and top < bottom:
        # Traverse from left to right along the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        
        # Traverse from top to bottom along the right column
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        
        if not (left < right and top < bottom):
            break
        
        # Traverse from right to left along the bottom row
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1
        
        # Traverse from bottom to top along the left column
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    
    return res