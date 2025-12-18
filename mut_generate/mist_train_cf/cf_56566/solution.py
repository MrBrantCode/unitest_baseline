"""
QUESTION:
Write a function `merge_lists(A, B)` that merges two distinct ascending-ordered lists of integers, A and B, of unequal lengths, into a single list in ascending order without using any built-in sort functions. The function should minimize comparisons for maximum efficiency.
"""

def merge_lists(A, B):
    merged_list = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged_list.append(A[i])
            i += 1
        else:
            merged_list.append(B[j])
            j += 1
    while i < len(A):
        merged_list.append(A[i])
        i += 1
    while j < len(B):
        merged_list.append(B[j])
        j += 1
    return merged_list