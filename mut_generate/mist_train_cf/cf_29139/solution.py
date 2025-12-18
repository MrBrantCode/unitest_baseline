"""
QUESTION:
Find the shortest superstring that contains all given fragments. A superstring is a string that contains all the given strings as substrings. Write a function `shortestSuperstring` that takes a list of strings as input and returns the shortest superstring. The input list contains only strings, and the output should be a string.
"""

from itertools import permutations

def shortestSuperstring(A):
    def overlap(a, b):
        max_overlap = 0
        for i in range(min(len(a), len(b)), -1, -1):
            if a.endswith(b[:i]):
                return i
        return max_overlap

    while len(A) > 1:
        max_overlap_len = 0
        to_merge = (0, 1)
        for i, j in permutations(range(len(A)), 2):
            overlap_len = overlap(A[i], A[j])
            if overlap_len > max_overlap_len:
                max_overlap_len = overlap_len
                to_merge = (i, j)

        i, j = to_merge
        A[i] += A[j][max_overlap_len:]
        A.pop(j)

    return A[0]