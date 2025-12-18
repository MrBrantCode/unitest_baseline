"""
QUESTION:
Write a function named `find_subset_in_order` that takes in two lists A and B as parameters, where A has n unique integers and B has m unique integers (m < n), and returns a tuple containing a boolean value indicating whether B's elements are all present in A in the same order and the starting index of the first occurrence of B in A. The function should not use any additional data structures. The length of list A will be in the range [1, 10^6] and the length of list B will be in the range [1, n-1].
"""

def find_subset_in_order(A, B):
    n = len(A)
    m = len(B)
    
    for i in range(n - m + 1):
        if A[i:i+m] == B:
            return (True, i)
    
    return (False, -1)