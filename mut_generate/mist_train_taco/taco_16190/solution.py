"""
QUESTION:
dot

The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11

cross

The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2

Task

You are given two arrays $\mbox{A}$ and $\mbox{B}$. Both have dimensions of $N$X$N$. 

Your task is to compute their matrix product.

Input Format

The first line contains the integer $N$. 

The next $N$ lines contains $N$ space separated integers of array $\mbox{A}$. 

The following $N$ lines contains $N$ space separated integers of array $\mbox{B}$.

Output Format

Print the matrix multiplication of $\mbox{A}$ and $\mbox{B}$.

Sample Input
2
1 2
3 4
1 2
3 4

Sample Output
[[ 7 10]
 [15 22]]
"""

import numpy as np

def matrix_multiplication(A, B):
    """
    Computes the matrix multiplication of two 2D arrays A and B.

    Parameters:
    A (list of lists): The first 2D array.
    B (list of lists): The second 2D array.

    Returns:
    numpy.ndarray: The result of the matrix multiplication of A and B.
    """
    return np.dot(A, B)