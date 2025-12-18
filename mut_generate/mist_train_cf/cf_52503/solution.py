"""
QUESTION:
Design a function `contains_element(A, B)` that takes two integer arrays `A` and `B` and returns `True` if `A` contains at least one element from `B`, and `False` otherwise. The function should be able to handle 2D arrays and should have a time complexity under O(n log n). Assume individual elements are considered separately when dealing with 2D arrays.
"""

def contains_element(A, B):
    A.sort()
    B.sort()

    i = j = 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] == B[j]:
            return True
        else:
            j += 1

    return False