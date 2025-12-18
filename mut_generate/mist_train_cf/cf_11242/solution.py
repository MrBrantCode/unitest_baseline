"""
QUESTION:
Write a function named `union` that takes two lists A and B as input, where A and B can contain duplicate elements and may not be sorted. The function should return a list containing the union of A and B, excluding duplicates, without using any built-in functions or libraries for set operations.
"""

def union(A, B):
    union_set = []
    
    for element in A:
        if element not in union_set:
            union_set.append(element)
    
    for element in B:
        if element not in union_set:
            union_set.append(element)
    
    return union_set