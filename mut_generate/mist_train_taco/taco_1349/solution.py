"""
QUESTION:
Given a matrix M of n*n size, the task is to complete the function which prints its elements in a diagonal pattern as depicted below.
 
 
Example 1:
Input:
N = 3
mat[][] = {{1 2 3},{4 5 6},{7 8 9}}
Output: 1 2 4 7 5 3 6 8 9
Example 2:
Input:
N = 2
mat[][] = {{1 2},{3 4}}
Output: 1 2 3 4
Your Task:
You only need to implement the given function matrixDiagonally() which returns a list containing the matrix diagonally. Do not read input, instead use the arguments given in the function. Print the elements in Matrix in a diagonal pattern.
Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(1)
Constraints:
1<=N<=100
"""

def matrix_diagonally(mat):
    n = len(mat)
    m = len(mat[0])
    diagonals = [[] for _ in range(n + m - 1)]
    
    for i in range(n):
        for j in range(m):
            sum_index = i + j
            if sum_index % 2 == 0:
                diagonals[sum_index].insert(0, mat[i][j])
            else:
                diagonals[sum_index].append(mat[i][j])
    
    result = []
    for diagonal in diagonals:
        result.extend(diagonal)
    
    return result