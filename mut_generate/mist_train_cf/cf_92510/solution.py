"""
QUESTION:
Write a function named `is_subset_in_order` that takes two lists A and B as parameters, where A has n unique integers and B has m unique integers (m < n), and returns a boolean value indicating whether B's elements are all present in A in the same order. The function should only use the input lists and no additional data structures. The length of A will be in the range [1, 10^6] and the length of B will be in the range [1, n-1].
"""

def is_subset_in_order(A, B):
    i = 0  # Pointer for list A
    j = 0  # Pointer for list B
    
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            j += 1  # Move pointer for list B
        i += 1  # Move pointer for list A
    
    return j == len(B)  # Return True if we reached the end of list B