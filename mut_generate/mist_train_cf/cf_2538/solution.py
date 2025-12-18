"""
QUESTION:
Write a function named `sum_of_neighbors` that takes a 2D matrix as input, where each element in the resulting matrix is the sum of the corresponding element in the input matrix and its neighboring elements (top, bottom, left, right, and diagonals). The input matrix is a list of lists, where each inner list has the same length.
"""

def sum_of_neighbors(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def get_neighbors(i, j):
        neighbors = []
        
        if i > 0:
            neighbors.append(matrix[i-1][j])  
            if j > 0:
                neighbors.append(matrix[i-1][j-1])  
            if j < cols-1:
                neighbors.append(matrix[i-1][j+1])  
        
        if i < rows-1:
            neighbors.append(matrix[i+1][j])  
            if j > 0:
                neighbors.append(matrix[i+1][j-1])  
            if j < cols-1:
                neighbors.append(matrix[i+1][j+1])  
        
        if j > 0:
            neighbors.append(matrix[i][j-1])  
        if j < cols-1:
            neighbors.append(matrix[i][j+1])  
        
        return neighbors
    
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(i, j)
            result[i][j] = sum(neighbors) + matrix[i][j]
    
    return result