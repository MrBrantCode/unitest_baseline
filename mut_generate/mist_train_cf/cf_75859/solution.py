"""
QUESTION:
Given two numerical sequences A and B of lengths up to 10^6, where the sequences may have different lengths and contain repetitive elements, write a function `count_common_pairs(A, B)` that returns the total count of pairs of indices (i, j) where A[i] equals B[j]. The function should be efficient enough to handle the maximum allowed sequence lengths within an acceptable computation duration.
"""

def count_common_pairs(A, B):
    indices_A = {}
    for i, a in enumerate(A):
        if a not in indices_A:
            indices_A[a] = []
        indices_A[a].append(i)

    common_pairs_count = 0
    for j, b in enumerate(B):
        if b in indices_A:
            common_pairs_count += len(indices_A[b])

    return common_pairs_count