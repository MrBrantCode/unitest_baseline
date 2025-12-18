"""
QUESTION:
Design a function called `find_pair` that takes a 2D matrix of positive integers and a target number as input. The function should find a pair of numbers in the matrix that sum up to the target number. The pair can be in any direction (horizontal, vertical, or diagonal). If a pair is found, return the pair of numbers. If no pair is found, return "No solution found". The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def find_pair(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    # Check horizontally
    for row in matrix:
        for i in range(len(row) - 1):  
            if row[i] + row[i + 1] == target:
                return [row[i], row[i + 1]]

    # Check vertically
    for i in range(rows - 1):  
        for j in range(cols):
            if matrix[i][j] + matrix[i + 1][j] == target:
                return [matrix[i][j], matrix[i + 1][j]]

    # Check diagonally 
    for i in range(rows - 1):  
        for j in range(cols - 1):  
            if matrix[i][j] + matrix[i + 1][j + 1] == target:
                return [matrix[i][j], matrix[i + 1][j + 1]]

    # Check counter-diagonally
    for i in range(rows - 1, 0, -1):  
        for j in range(cols - 1):  
            if matrix[i][j] + matrix[i - 1][j + 1] == target:
                return [matrix[i][j], matrix[i - 1][j + 1]]

    # If no solution found
    return "No solution found"