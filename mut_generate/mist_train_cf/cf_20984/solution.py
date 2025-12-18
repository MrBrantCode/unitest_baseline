"""
QUESTION:
Write a function named `spiral_sum` that takes a 2D matrix as input and returns the sum of all positive numbers in the matrix when traversed in a spiral form. The function should skip over any negative numbers in the matrix. The input matrix is a list of lists of integers, and the output should be a single integer representing the sum of the positive numbers.
"""

def spiral_sum(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    sums = 0
    
    # Define the directions for traversal
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0
    row, col = 0, 0
    
    while True:
        if not visited[row][col] and matrix[row][col] > 0:
            sums += matrix[row][col]
        visited[row][col] = True
        
        # Try to move in the current direction
        next_row, next_col = row + directions[direction_idx][0], col + directions[direction_idx][1]
        
        # If the next position is out of bounds or has been visited, change direction
        if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or visited[next_row][next_col]:
            direction_idx = (direction_idx + 1) % 4
        
        # Move in the current direction
        row, col = row + directions[direction_idx][0], col + directions[direction_idx][1]
        
        # If all elements have been visited, break the loop
        if all(visited[i][j] for i in range(rows) for j in range(cols)):
            break
    
    return sums