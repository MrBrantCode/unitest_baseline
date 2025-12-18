"""
QUESTION:
Create a function `delete(A, B)` that takes two strings `A` and `B` as input. The function should return a new string where all characters in `A` that are also present in `B` are removed.
"""

def delete(A, B):
    for i in B:
        if i in A:
            A = A.replace(i, '')
    return A