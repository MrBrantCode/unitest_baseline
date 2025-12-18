"""
QUESTION:
Write a function `merge_sorted_arrays` that combines two pre-sorted arrays `A` and `B` into a single sorted array. The function should run in linear time complexity O(n), where n is the total number of elements in the two arrays. The input arrays are already sorted in ascending order.
"""

def merge_sorted_arrays(A, B):
    i = 0
    j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i < len(A):
        C.extend(A[i:])
    if j < len(B):
        C.extend(B[j:])
    return C