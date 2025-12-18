"""
ORIGINAL QUESTION:
Write a function `cartesian_product(A: set, B: set) -> set` that returns the Cartesian product of two sets A and B as a set. The function should have a time complexity of O(n * m), where n is the number of elements in set A and m is the number of elements in set B. The sets A and B have at most 10^5 elements each.
"""

def entance(A: set, B: set) -> set:
    cartesian_set = set()
    
    for a in A:
        for b in B:
            cartesian_set.add((a, b))
    
    return cartesian_set