"""
QUESTION:
Write a function `delete_chars(A, B)` that takes two strings `A` and `B` as input and returns a modified string `A` where all characters that appear in `B` or appear more than once consecutively in `A` are deleted.
"""

def delete_chars(A, B):
    A = list(A)
    B = list(B)
    i = 0
    while i < len(A):
        if A[i] in B or (i > 0 and A[i] == A[i-1]):
            del A[i]
        else:
            i += 1
    return ''.join(A)