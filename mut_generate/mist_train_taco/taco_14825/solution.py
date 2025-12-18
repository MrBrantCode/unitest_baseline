"""
QUESTION:
Given a N x N 2D matrix Arr representing an image. Rotate the image by 90 degrees (anti-clockwise). You need to do this in place. Note that if you end up using an additional array, you will only receive partial score.
Example 1:
Input:
N = 3
Arr[][] = {{1,  2,  3}
           {4,  5,  6}
           {7,  8,  9}}
Output:
 3  6  9 
 2  5  8 
 1  4  7 
Explanation: The given matrix is rotated
by 90 degree in anti-clockwise direction.
Example 2:
Input:
N = 4
Arr[][] = {{1,  2,  3,  4}
           {5,  6,  7,  8}
           {9, 10, 11, 12}
           {13, 14, 15, 16}}
Output:
 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13
Explanation: The given matrix is rotated
by 90 degree in anti-clockwise direction.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function rotate() which takes the 2D array of integers arr and n as parameters and returns void. You need to change the array itself.
Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 1000
1 ≤ Arr[i][j] ≤ 1000
"""

def rotate_matrix_anticlockwise(arr, n):
    # Create a new list to store the rotated matrix
    rotated = []
    
    # Iterate over each column from the last to the first
    for col in range(n-1, -1, -1):
        # Create a new row for the rotated matrix
        new_row = []
        # Iterate over each row from the first to the last
        for row in range(n):
            # Append the element from the current column and row to the new row
            new_row.append(arr[row][col])
        # Append the new row to the rotated matrix
        rotated.append(new_row)
    
    # Update the original matrix with the rotated matrix
    for i in range(n):
        arr[i] = rotated[i]