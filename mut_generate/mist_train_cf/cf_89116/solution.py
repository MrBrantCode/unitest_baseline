"""
QUESTION:
Given two lists A and B of unique integers, where A contains n integers and B contains m integers (m < n), implement a function `find_subset_in_order` that takes A and B as parameters and returns a tuple containing a boolean value indicating whether B's elements are all present in A in the same order and the starting index of the first occurrence of B in A. The time complexity should be O(n + m) and the space complexity should be O(1).
"""

def find_subset_in_order(A, B):
    n = len(A)
    m = len(B)
    
    i = 0
    j = 0
    start_index = -1
    
    while i < n and j < m:
        if A[i] == B[j]:
            if start_index == -1:
                start_index = i
            j += 1
        i += 1
    
    if j == m:
        return True, start_index
    else:
        return False, -1