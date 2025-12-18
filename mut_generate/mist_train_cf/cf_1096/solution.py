"""
QUESTION:
Write a function `get_adjacent_numbers(matrix)` to return an array of adjacent numbers (horizontally, vertically, and diagonally) in a given two-dimensional array `matrix`. The function should work with non-square matrices and exclude duplicate numbers from the output array.
"""

def get_adjacent_numbers(matrix):
    adjacent_numbers = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Iterate over each element in the matrix
    for i in range(rows):
        for j in range(cols):
            num = matrix[i][j]
            
            # Check the adjacent elements in all directions
            if i > 0:
                adjacent_numbers.append(matrix[i-1][j]) # Up
            if i < rows-1:
                adjacent_numbers.append(matrix[i+1][j]) # Down
            if j > 0:
                adjacent_numbers.append(matrix[i][j-1]) # Left
            if j < cols-1:
                adjacent_numbers.append(matrix[i][j+1]) # Right
            if i > 0 and j > 0:
                adjacent_numbers.append(matrix[i-1][j-1]) # Diagonal: Up-Left
            if i > 0 and j < cols-1:
                adjacent_numbers.append(matrix[i-1][j+1]) # Diagonal: Up-Right
            if i < rows-1 and j > 0:
                adjacent_numbers.append(matrix[i+1][j-1]) # Diagonal: Down-Left
            if i < rows-1 and j < cols-1:
                adjacent_numbers.append(matrix[i+1][j+1]) # Diagonal: Down-Right
    
    # Remove duplicates and return the result
    return list(set(adjacent_numbers))