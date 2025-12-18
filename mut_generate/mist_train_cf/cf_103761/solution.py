"""
QUESTION:
Write a function `kth_smallest_element(A, B, k)` that takes two sorted lists A and B, and an integer k, and returns the k-th smallest element in the combined list. The function should assume that k is within the bounds of the combined list and that the input lists A and B are non-empty and sorted in ascending order.
"""

def findKth(A, B, k):
    len_A = len(A)
    len_B = len(B)
    i = 0  # Pointer for array A
    j = 0  # Pointer for array B
    count = 0  # Counter for the k-th smallest element
    
    while i < len_A and j < len_B:
        if A[i] < B[j]:
            smallest = A[i]
            i += 1
        else:
            smallest = B[j]
            j += 1
        
        count += 1
        if count == k:
            return smallest
    
    # If one array is exhausted, but the other still has elements
    while i < len_A:
        smallest = A[i]
        i += 1
        count += 1
        if count == k:
            return smallest
    
    while j < len_B:
        smallest = B[j]
        j += 1
        count += 1
        if count == k:
            return smallest