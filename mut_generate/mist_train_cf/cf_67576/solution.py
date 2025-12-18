"""
QUESTION:
Given a permutation A of [0, 1, ..., N - 1], determine if the count of global inversions equals the count of local inversions. Return true if they are equal, false otherwise. A will be a permutation of [0, 1, ..., A.length - 1] and will have a length within the range [1, 5000].
"""

def isIdealPermutation(A):
    max_seen_so_far = -1
    for i in range(len(A) - 2):
        max_seen_so_far = max(max_seen_so_far, A[i])
        if max_seen_so_far > A[i + 2]:
            return False
    return True