"""
QUESTION:
Concatenate  

Two or more arrays can be concatenated together using the concatenate function with a
tuple of the arrays to be joined:

import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]

If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.

import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]    

Task  

You are given two integer arrays of size $N$X$\mbox{P}$ and $\mbox{M}$X$\mbox{P}$ ($N$ & $\mbox{M}$ are rows, and $\mbox{P}$ is the column).  Your task is to concatenate the arrays along axis $\mbox{o}$.

Input Format

The first line contains space separated integers $N$, $\mbox{M}$ and $\mbox{P}$. 

The next $N$ lines contains the space separated elements of the $\mbox{P}$ columns. 

After that, the next $\mbox{M}$ lines contains the space separated elements of the $\mbox{P}$ columns.

Output Format

Print the concatenated array of size $(N+M)$X$\mbox{P}$.

Sample Input
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

Sample Output
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]
"""

import numpy as np

def concatenate_arrays(arr_N, arr_M, axis=0):
    """
    Concatenates two 2D numpy arrays along the specified axis.

    Parameters:
    arr_N (numpy.ndarray): A 2D array of size N x P.
    arr_M (numpy.ndarray): A 2D array of size M x P.
    axis (int): The axis along which the arrays are concatenated. Default is 0.

    Returns:
    numpy.ndarray: A 2D array of size (N+M) x P.
    """
    return np.concatenate((arr_N, arr_M), axis=axis)