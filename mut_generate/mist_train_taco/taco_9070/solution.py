"""
QUESTION:
Transpose means is to interchange rows and columns of a two-dimensional array matrix.

[A^(T)]ij=[A]ji

ie:
Formally, the i th row, j th column element of AT is the j th row, i th column element of A:



Example :

```
[[1,2,3],[4,5,6]].transpose() //should return [[1,4],[2,5],[3,6]]
```

Write a prototype transpose to array in JS or add a .transpose method in Ruby or create a transpose function in Python so that any matrix of order ixj 2-D array returns transposed Matrix of jxi .

Link:  To understand array prototype
"""

def transpose_matrix(A):
    """
    Transposes a given 2-dimensional matrix.

    Parameters:
    A (list of lists): A 2-dimensional list (matrix) to be transposed.

    Returns:
    list of lists: The transposed matrix.
    """
    if not A:
        return []
    
    # Use list comprehension to transpose the matrix
    transposed = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    
    return transposed