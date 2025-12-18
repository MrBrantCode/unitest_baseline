"""
QUESTION:
Given two arrays A and B of equal length, write a function `matchIndices(A, B)` that determines if there exists a pair of indices (i, j) where A[i] equals B[j]. The function should return a boolean indicating whether such a pair exists, along with the pair of indices if it does, or an empty tuple if it does not.
"""

def matchIndices(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                return True, (i, j)
    return False, ()