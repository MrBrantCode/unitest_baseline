"""
QUESTION:
Write a function `find_index_match(A, B)` that takes two identically dimensioned sequences A and B, and returns the first pair of indices (i, j) where A[i] equals B[j]. If no such pair exists, return None.
"""

def find_index_match(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                return (i, j) 
    return None 