"""
QUESTION:
Write a function `traverse_matrix(matrix)` that takes a 2D list of integers as input and returns a tuple containing the sum of all positive numbers and the count of negative numbers in the matrix. The function should traverse the matrix in a spiral form, skipping over any negative numbers in the sum calculation. The function should be able to handle matrices of arbitrary dimensions efficiently, with a time complexity of O(n), where n is the total number of elements in the matrix, and a space complexity of O(1).
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