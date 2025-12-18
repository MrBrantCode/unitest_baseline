"""
QUESTION:
Write a function named `compute_union(A, B)` to compute the union of two sets A and B using algorithms. The function should not use any built-in functions or libraries for set operations. The input sets can contain duplicate elements and may not be sorted. The solution should have a time complexity of O(n+m), where n and m are the lengths of sets A and B respectively. The solution should use only constant extra space, excluding the space required for the output.
"""

def compute_union(A, B):
    C = []
    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        elif B[j] < A[i]:
            C.append(B[j])
            j += 1
        else:  
            C.append(A[i])
            i += 1
            j += 1

    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1

    return C