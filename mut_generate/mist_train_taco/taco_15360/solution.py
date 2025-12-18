"""
QUESTION:
Given a square matrix[][] of size N x N. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space.
Example 1:
Input:
N = 3
matrix[][] = [[1 2 3],
              [4 5 6],
              [7 8 9]]
Output:
3 6 9 
2 5 8 
1 4 7
Your Task:
You only need to implement the given function rotate(). Do not read input, instead use the arguments given in the function. 
Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 50
1 <= matrix[][] <= 100
"""

def rotate_matrix_anticlockwise(matrix):
    N = len(matrix)
    l = []
    for i in range(-1, -(N + 1), -1):
        k = []
        for j in range(N):
            k.append(matrix[j][i])
        l.append(k)
    for i in range(N):
        matrix[i] = l[i]