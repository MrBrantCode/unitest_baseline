"""
QUESTION:
Convert the given matrix into a list of lists. The matrix has n rows and m columns, where n and m are positive integers. The elements in each row are in ascending order, and the elements in each column are in descending order. The function should be named "matrix_to_list" and take as input the matrix and the number of rows (n) and columns (m). Implement the solution with a time complexity of O(n+m).
"""

def matrix_to_list(matrix, n, m):
    result = []
    row = n - 1
    col = 0

    while row >= 0 and col < m:
        current_row = []
        
        while row >= 0:
            current_row.append(matrix[row][col])
            row -= 1
        
        result.append(current_row)
        col += 1
        row = n - 1
    
    return result