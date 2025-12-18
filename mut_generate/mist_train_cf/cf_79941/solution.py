"""
QUESTION:
Implement a function `strassen(A, B)` that performs Strassen's Algorithm to multiply two given square matrices `A` and `B` of order `n x n`, where `n` may not necessarily be a power of 2. The function should handle cases of non-square matrices by padding them with zeros to the nearest power of 2. The function should optimize for space complexity and return the resulting matrix. Assume that both input matrices have the same dimensions.
"""

import numpy as np

def strassen(A, B):
    # find size n, that is power of 2 and is higher than original size
    n = max(np.shape(A)[0], np.shape(B)[0])
    n = 2**np.ceil(np.log2(n))

    # pad matrix with zeros
    A = np.pad(A, [(0, int(n - np.shape(A)[0])), (0, int(n - np.shape(A)[1]))], mode = 'constant')
    B = np.pad(B, [(0, int(n - np.shape(B)[0])), (0, int(n - np.shape(B)[1]))], mode = 'constant')

    # Base case of recursive function
    if np.shape(A)[0] == 1:
        return A * B

    # Split the matrix into four parts
    mid = np.shape(A)[0]//2
    a11, a12, a21, a22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    b11, b12, b21, b22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Recursive calls for the seven products
    p1 = strassen(a11, b12 - b22)
    p2 = strassen(a11 + a12, b22)
    p3 = strassen(a21 + a22, b11)
    p4 = strassen(a22, b21 - b11)
    p5 = strassen(a11 + a22, b11 + b22)
    p6 = strassen(a12 - a22, b21 + b22)
    p7 = strassen(a11 - a21, b11 + b12)

    # Forming resultant matrix
    C = np.empty(np.shape(A))
    C[:mid, :mid] = p5 + p4 - p2 + p6
    C[:mid, mid:] = p1 + p2
    C[mid:, :mid] = p3 + p4
    C[mid:, mid:] = p1 + p5 - p3 - p7

    return C