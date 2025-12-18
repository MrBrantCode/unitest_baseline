"""
QUESTION:
Write a function `traverse_matrix(matrix)` that takes an input matrix of arbitrary dimensions as input and traverses it in a spiral form. The function should keep track of the sum of all positive numbers in the matrix and the count of negative numbers encountered. It should skip over any negative numbers in the matrix and only consider the positive numbers in the sum calculation. The function should return both the sum of positive numbers and the count of negative numbers encountered. The function must have a time complexity of O(n), where n is the total number of elements in the matrix, and a space complexity of O(1), not using any additional data structures that depend on the size of the input matrix.
"""

def traverse_matrix(matrix):
    rows = len(matrix)
    if rows == 0:
        return 0, 0
    cols = len(matrix[0])
    
    # Initialize variables
    total_sum = 0
    negative_count = 0
    
    # Define boundaries
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    
    # Traverse matrix in a spiral form
    while top <= bottom and left <= right:
        # Traverse top row
        for i in range(left, right + 1):
            if matrix[top][i] > 0:
                total_sum += matrix[top][i]
            elif matrix[top][i] < 0:
                negative_count += 1
        top += 1
        
        # Traverse right column
        for i in range(top, bottom + 1):
            if matrix[i][right] > 0:
                total_sum += matrix[i][right]
            elif matrix[i][right] < 0:
                negative_count += 1
        right -= 1
        
        # Traverse bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                if matrix[bottom][i] > 0:
                    total_sum += matrix[bottom][i]
                elif matrix[bottom][i] < 0:
                    negative_count += 1
            bottom -= 1
        
        # Traverse left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                if matrix[i][left] > 0:
                    total_sum += matrix[i][left]
                elif matrix[i][left] < 0:
                    negative_count += 1
            left += 1
    
    return total_sum, negative_count