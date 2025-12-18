"""
QUESTION:
Create a function named `function` that takes an integer `n` as input. The function should create an NxN matrix and fill it with sequential numbers from 0 to N^2 - 1, then rotate the matrix 90 degrees clockwise. Finally, the function should check if the rotated matrix is symmetrical and return True if it is, and False otherwise. Note that the input matrix will always be a square matrix, but it will never be symmetrical due to its sequential numbering.
"""

def function(n):
    """This function creates an NxN matrix, fills it with sequential numbers from 0 to N^2 - 1, 
    rotates the matrix 90 degrees clockwise, and checks if the rotated matrix is symmetrical."""
    
    # Create an NxN matrix and fill it with sequential numbers from 0 to N^2 - 1
    matrix = [[i * n + j for j in range(n)] for i in range(n)]
    
    # Rotate the matrix 90 degrees clockwise
    matrix = [list(value) for value in zip(*matrix[::-1])]
    
    # Check if the rotated matrix is symmetrical
    return matrix == list(map(list, zip(*matrix)))