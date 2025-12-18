"""
QUESTION:
Given two lists A and B of unique integers, where the length of A is n and the length of B is m (m < n), write a function `find_subset_in_order` that takes A and B as input and returns a tuple containing a boolean value indicating whether B's elements are all present in A in the same order and the starting index of the first occurrence of B in A. The function should not use any additional data structures and should handle lists A and B where 1 ≤ n ≤ 10^6 and 1 ≤ m < n.
"""

def find_subset_in_order(A, B):
    n = len(A)
    m = len(B)
    
    for i in range(n - m + 1):
        if A[i:i+m] == B:
            return (True, i)
    
    return (False, -1)