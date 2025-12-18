"""
QUESTION:
Write a function `compute_union(A, B)` that takes two lists A and B as input, which can contain duplicate elements and are not necessarily sorted, and returns their union without using any built-in functions or libraries for set operations. The function should have a time complexity of O(n+m), where n and m are the lengths of A and B respectively, and use only constant extra space, excluding the space required for the output.
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