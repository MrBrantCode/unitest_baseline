"""
QUESTION:
Design a function named "rotate" that takes a 2D list "mat" representing a square matrix and an integer "pos" representing the number of positions to rotate the matrix clockwise. The function should return the rotated matrix. The matrix should only contain integers. If the input is not a square matrix or contains non-integer values, or if the number of positions is not a positive integer, the function should return an error message.
"""

def rotate(mat, pos):
    if type(mat) is not list or len(mat) == 0 or len(mat) != len(mat[0]):
        return "Error: Input is not a square matrix"
        
    if type(pos) is not int or pos < 0:
        return "Error: Positions for rotation is not a positive integer"
        
    for lst in mat:
        if type(lst) is not list or any(type(i) is not int for i in lst):
            return "Error: Matrix contains non-integer or incorrect entry"
            
    for _ in range(pos):
        # transpose the matrix
        mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))] 
        
        # reverse each row
        mat = [i[::-1] for i in mat]
    
    return mat