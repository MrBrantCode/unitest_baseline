"""
QUESTION:
Write a function that accepts a square matrix (`N x N` 2D array) and returns the determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

A 1x1 matrix `|a|` has determinant `a`.

A 2x2 matrix `[ [a, b], [c, d] ]` or
```
|a  b|
|c  d|
```
has determinant: `a*d - b*c`.

The determinant of an `n x n` sized matrix is calculated by reducing the problem to the calculation of the determinants of `n` matrices of`n-1 x n-1` size.

For the 3x3 case, `[ [a, b, c], [d, e, f], [g, h, i] ]` or
```
|a b c|  
|d e f|  
|g h i|  
```
the determinant is: `a * det(a_minor) - b * det(b_minor) + c * det(c_minor)` where `det(a_minor)` refers to taking the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs:
```
|- - -|
|- e f|
|- h i|  
```
Note the alternation of signs. 

The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row `[a, b, c, d]`, then:

`det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)`
"""

def calculate_determinant(matrix):
    # Base case for 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]
    
    # Initialize determinant
    det = 0
    
    # Iterate over the first row of the matrix
    for n in range(len(matrix)):
        # Create the minor matrix by excluding the current row and column
        minor = [row[:n] + row[n+1:] for row in matrix[1:]]
        
        # Calculate the determinant recursively
        minor_det = calculate_determinant(minor)
        
        # Alternate signs and add/subtract the product of the element and its minor's determinant
        if (n + 1) % 2 == 0:
            det -= matrix[0][n] * minor_det
        else:
            det += matrix[0][n] * minor_det
    
    return det