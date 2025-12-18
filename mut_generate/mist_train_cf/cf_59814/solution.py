"""
QUESTION:
Given a sorted array, design a function `remove_duplicates(A)` that removes duplicate elements in-place without using any extra memory and returns the new length of the modified array.
"""

def remove_duplicates(A):
    if len(A) == 0:
        return 0
    
    new_len = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            A[new_len] = A[i]
            new_len += 1
            
    return new_len