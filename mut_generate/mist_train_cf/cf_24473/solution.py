"""
QUESTION:
Implement a function named `merge_sort` that takes a list of elements as input and returns a sorted list using the merge sort algorithm. The function should recursively divide the input list into two halves until each sublist contains only one element, and then merge the sublists in a sorted manner.
"""

def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)

def merge(B, C):
    D = []
    while B and C:
        if B[0] <= C[0]:
            D.append(B.pop(0))
        else:
            D.append(C.pop(0))
    D.extend(B)
    D.extend(C)
    return D