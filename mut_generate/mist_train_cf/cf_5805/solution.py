"""
QUESTION:
Write a function named `find_subset_in_order` that takes in two lists A and B as parameters, where A contains n integers and B contains m integers (m < n), and returns a tuple containing a boolean value indicating whether B's elements are all present in A in the same order and the starting index of the first occurrence of B in A.

The function should satisfy the following constraints: 
- The length of list A (n) will be in the range [1, 10^6] and the length of list B (m) will be in the range [1, n-1].
- The elements in list A will be unique integers and the elements in list B will be unique integers.
- The time complexity of the function should be O(n + m), where n is the length of list A and m is the length of list B.
- The space complexity of the function should be O(1), meaning that the function should not use any additional data structures.
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