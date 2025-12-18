"""
QUESTION:
Given an NxM 2D matrix, rearrange such that 
Each diagonal in the lower left triangle of the rectangular grid is sorted in ascending order. 
Each diagonal in the upper right triangle of the rectangular grid is sorted in descending order. 
The major diagonal in the grid starting from the top-left corner is not rearranged. 
Example 1:
Input:
N = 4, M = 5 
matrix = {{3 6 3 8 2},
          {4 1 9 5 9},
          {5 7 2 4 8},
          {8 3 1 7 6}}
Output:
3 9 8 9 2
1 1 6 5 8
3 4 2 6 3
8 5 7 7 4
Explanation:
Before:
After:
Your Task:
You don't need to read input or print anything. Your task is to complete the function diagonalSort() which takes the matrix, n and m as input parameter and rearranges the elements of the matrix.
Expected Time Complexity: O(NxM)
Expected Auxiliary Space: O(N+M)
Constraints:
1 <= N,M <= 10^{4 }, 1<=N*M<=10^{5}
1 <= matrix[i] <= 10^{3}
"""

def diagonal_sort(matrix, n, m):
    # Dictionary to store diagonals
    diagonals = {}
    
    # Populate the dictionary with diagonals
    for i in range(n):
        for j in range(m):
            if (i - j) not in diagonals:
                diagonals[i - j] = [matrix[i][j]]
            else:
                diagonals[i - j].append(matrix[i][j])
    
    # Sort the diagonals
    for key, value in diagonals.items():
        if key > 0:
            value.sort(reverse=True)
        elif key < 0:
            value.sort()
        else:
            value[:] = value[::-1]
    
    # Reconstruct the matrix with sorted diagonals
    for i in range(n):
        for j in range(m):
            matrix[i][j] = diagonals[i - j].pop()