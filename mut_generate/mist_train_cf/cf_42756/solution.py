"""
QUESTION:
Implement the `largestOverlap` function which takes two square matrices A and B of the same size (n x n, 1 <= n <= 100) containing only 0s and 1s as input. Return the largest possible overlap between the two matrices by sliding A over B or B over A in any direction, defined as the number of 1s common in the overlapping regions of A and B.
"""

from collections import Counter

def largestOverlap(A, B):
    n = len(A)
    count = Counter()
    max_overlap = 0

    for i in range(n):
        for j in range(n):
            if A[i][j] == 1:
                for x in range(n):
                    for y in range(n):
                        if B[x][y] == 1:
                            count[(i - x, j - y)] += 1
                            max_overlap = max(max_overlap, count[(i - x, j - y)])

    return max_overlap