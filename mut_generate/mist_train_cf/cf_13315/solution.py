"""
QUESTION:
Write a function `spiral_matrix` that calculates the sum of all elements in a given matrix by traversing it in a spiral order from the outermost elements to the innermost elements. The matrix is a 2D list of integers. The function should return the total sum of all elements. The matrix is guaranteed to be a rectangle (i.e., all rows have the same number of columns) and is not empty.
"""

def spiral_matrix(matrix):
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    
    direction = 0
    
    total_sum = 0
    
    while top <= bottom and left <= right:
        
        if direction == 0:
            for i in range(left, right+1):
                total_sum += matrix[top][i]
            top += 1
            
        elif direction == 1:
            for i in range(top, bottom+1):
                total_sum += matrix[i][right]
            right -= 1
            
        elif direction == 2:
            for i in range(right, left-1, -1):
                total_sum += matrix[bottom][i]
            bottom -= 1
            
        elif direction == 3:
            for i in range(bottom, top-1, -1):
                total_sum += matrix[i][left]
            left += 1
            
        direction = (direction + 1) % 4
    
    return total_sum