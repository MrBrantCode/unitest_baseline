"""
QUESTION:
Given two arrays A and B of equal length, write a function `advantageCount(A, B)` that generates a permutation of A to maximize its advantage over B, where the advantage is the count of indices i where A[i] is greater than B[i]. The function must take into account the constraints: `1 <= A.length = B.length <= 10000` and `0 <= A[i], B[i] <= 10^9`.
"""

def advantageCount(A, B):
    sortedA = sorted(A)
    sortedB = sorted((b, i) for i, b in enumerate(B))
    res = [0] * len(A)
    lo = 0
    hi = len(A) - 1
    for b, i in sortedB[::-1]:
        if b < sortedA[hi]:
            res[i] = sortedA[hi]
            hi -= 1
        else:
            res[i] = sortedA[lo]
            lo += 1
    return res