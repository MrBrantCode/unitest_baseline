"""
QUESTION:
Given a matrix as 2D array. Find the reverse spiral traversal of the matrix. 
Example 1:
Input: R = 3, C = 3
  a = {{9, 8, 7},
       {6, 5, 4},
       {3, 2, 1}}
Output: 5 6 3 2 1 4 7 8 9
Explanation: Spiral form of the matrix
in reverse order starts from the centre 
and goes outward.
Example 2:
Input: R = 4, C = 4 
  a = {{1, 2, 3, 4},
       {5, 6, 7, 8},
       {9, 10, 11, 12}, 
       {13, 14, 15, 16}}
Output: 10 11 7 6 5 9 13 14 15 16 12 8 4 3 2 1
Explanation: 
Your Task:  
You dont need to read input or print anything. Complete the function reverseSpiral() which takes R, C and a as input parameters and returns the matrix in reverse spiral form.
Expected Time Complexity: O(R*C)
Expected Auxiliary Space: O(R*C)
Constraints:
1 <= R,C <=100
1 <= a[R][C] <=100
"""

def reverse_spiral_traversal(R, C, a):
    top, left = 0, 0
    bottom, right = R - 1, C - 1
    ans = []
    
    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for i in range(left, right + 1):
            ans.append(a[top][i])
        top += 1
        
        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            ans.append(a[i][right])
        right -= 1
        
        # Traverse from right to left along the bottom row, if still within bounds
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(a[bottom][i])
            bottom -= 1
        
        # Traverse from bottom to top along the left column, if still within bounds
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(a[i][left])
            left += 1
    
    # Reverse the collected elements to get the reverse spiral order
    ans.reverse()
    return ans