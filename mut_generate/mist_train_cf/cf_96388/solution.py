"""
QUESTION:
Write a function named `spiral_sum` that takes a 2D matrix as input and returns the sum of all positive numbers in the matrix when traversed in a spiral order, skipping any negative numbers. The function should work for any size of matrix and should not traverse a cell more than once.
"""

def spiral_sum(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    sums = 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0
    row, col = 0, 0
    
    while True:
        if not visited[row][col] and matrix[row][col] > 0:
            sums += matrix[row][col]
        visited[row][col] = True
        
        next_row, next_col = row + directions[direction_idx][0], col + directions[direction_idx][1]
        
        if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or visited[next_row][next_col]:
            direction_idx = (direction_idx + 1) % 4
        
        row, col = row + directions[direction_idx][0], col + directions[direction_idx][1]
        
        if all(visited[i][j] for i in range(rows) for j in range(cols)):
            break
    
    return sums