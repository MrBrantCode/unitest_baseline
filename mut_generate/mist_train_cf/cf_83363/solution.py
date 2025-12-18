"""
QUESTION:
Given two arrays A and B of lengths n and m, respectively, where n and m can be up to 10^6, determine the total number of index pairs (i, j) such that A[i] equals B[j]. Write a function `find_pairs(A, B)` to solve this problem efficiently. The function should return the total number of such index pairs.
"""

def find_pairs(A, B):
    # Step 1 and Step 2
    setA = set(A)
    
    # Step 3
    counter = 0
    
    # Step 4
    for b in B:
        if b in setA:
            counter += 1
    
    # Step 5
    return counter