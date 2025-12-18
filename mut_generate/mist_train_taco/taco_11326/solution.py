"""
QUESTION:
The NumPy module also comes with a number of built-in routines for linear algebra calculations. These can be found in the sub-module linalg.  

linalg.det

The linalg.det tool computes the determinant of an array.  

print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0

linalg.eig

The linalg.eig computes the eigenvalues and right eigenvectors of a square array.    

vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print vals                                      #Output : [ 3. -1.]
print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]

linalg.inv  

The linalg.inv tool computes the (multiplicative) inverse of a matrix.

print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]

Other routines can be found here

Task

You are given a square matrix $\mbox{A}$ with dimensions $N$X$N$. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

Input Format

The first line contains the integer $N$. 

The next $N$ lines contains the $N$ space separated elements of array $\mbox{A}$. 

Output Format

Print the determinant of $\mbox{A}$.

Sample Input
2
1.1 1.1
1.1 1.1

Sample Output
0.0
"""

import numpy as np

def compute_determinant(matrix):
    """
    Computes the determinant of a given square matrix and rounds the result to 2 decimal places.

    Parameters:
    matrix (list of lists or numpy.ndarray): A 2D list or NumPy array representing the square matrix.

    Returns:
    float: The determinant of the matrix, rounded to 2 decimal places.
    """
    # Convert the input matrix to a NumPy array if it's not already
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix)
    
    # Compute the determinant
    det = np.linalg.det(matrix)
    
    # Round the determinant to 2 decimal places
    det_rounded = round(det, 2)
    
    return det_rounded