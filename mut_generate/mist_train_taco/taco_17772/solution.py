"""
QUESTION:
Given a matrix of  size n x m. Your task is to make Zeroes, that means in whole matrix when you find a zero, convert its upper, lower, left, and right value to zero and make that element the sum of the upper, lower, left and right value. Do the following tasks according to the initial matrix.
 
Example 1:
Input: matrix = {{1, 2, 3, 4},
                 {5, 6, 0, 7}, 
                 {8, 9, 4, 6},
                 {8, 4, 5, 2}}
Output: {{1, 2, 0, 4}, 
         {5, 0, 20, 0},
         {8, 9, 0, 6}, 
         {8, 4, 5, 2}}
Explanation: As matrix[1][2] = 0, we will
perform the operation here. Then matrix[1][2]
= matrix[0][2] + matrix[2][2] + matrix[1][1] 
+ matrix[1][3] and matrix[0][2] = matrix[2][2] 
= matrix[1][1] = matrix[1][3] = 0.
Example 2:
Input: matrix = {{1, 2}, 
                 {3, 4}}
output: {{1, 2}, 
         {3, 4}}
Your Task:
You don't need to read or print anything. Your task is to complete the function MakeZeros() which takes the matrix as input parameter and does the given task according to initial matrix. You don't need to return anything. The driver code prints the modified matrix itself in the output.
 
Expected Time Complexity: O(n * m)
Expected Space Complexity: O(n * m)
 
Constraints:
1 ≤ n, m ≤ 100
0 ≤ matrix[i][j] ≤ 100, where 0 ≤ i ≤ n and 0 ≤ j ≤ m
"""

import copy

def make_zeros(matrix):
    """
    Modifies the input matrix such that when a zero is found, its upper, lower, left, and right values are converted to zero,
    and the zero element is replaced by the sum of its upper, lower, left, and right values.

    Parameters:
    matrix (list of list of int): The input matrix to be modified.

    Returns:
    None: The matrix is modified in place.
    """
    zero_coordinates = []
    hash_map = {}
    (m, n) = (len(matrix), len(matrix[0]))
    new_matrix = copy.deepcopy(matrix)
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_coordinates.append((i, j))
            hash_map[i, j] = matrix[i][j]
    
    for coordinate in zero_coordinates:
        dr = [-1, 0, 1, 0]
        dc = [0, -1, 0, 1]
        total_sum = 0
        for i in range(4):
            new_row = coordinate[0] + dr[i]
            new_col = coordinate[1] + dc[i]
            if 0 <= new_row < m and 0 <= new_col < n:
                total_sum += hash_map[new_row, new_col]
                matrix[new_row][new_col] = 0
        matrix[coordinate[0]][coordinate[1]] = total_sum