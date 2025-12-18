"""
QUESTION:
Write a function `spiral_matrix(matrix)` that takes a 2D list `matrix` as input and returns the sum of all elements in the matrix when traversed in spiral order. The function should handle matrices of any size.
"""

def spiral_matrix(matrix):
    # Define the boundaries of the matrix
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    
    # Define the direction of traversal
    direction = 0
    # 0 - moving left to right
    # 1 - moving top to bottom
    # 2 - moving right to left
    # 3 - moving bottom to top
    
    # Initialize the sum
    total_sum = 0
    
    # Iterate until all elements are visited
    while top <= bottom and left <= right:
        
        if direction == 0:
            # Traverse from left to right
            for i in range(left, right+1):
                total_sum += matrix[top][i]
            top += 1
            
        elif direction == 1:
            # Traverse from top to bottom
            for i in range(top, bottom+1):
                total_sum += matrix[i][right]
            right -= 1
            
        elif direction == 2:
            # Traverse from right to left
            for i in range(right, left-1, -1):
                total_sum += matrix[bottom][i]
            bottom -= 1
            
        elif direction == 3:
            # Traverse from bottom to top
            for i in range(bottom, top-1, -1):
                total_sum += matrix[i][left]
            left += 1
            
        # Update the direction for the next iteration
        direction = (direction + 1) % 4
    
    return total_sum