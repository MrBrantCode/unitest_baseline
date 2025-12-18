"""
QUESTION:
Write a function `cartesian_product(A: set, B: set) -> set` that returns the Cartesian product of two sets A and B as a set. The Cartesian product is defined as the set of all possible ordered pairs (a, b) where a is an element of A and b is an element of B. The function should return the Cartesian product without including any duplicate elements and the order of the elements does not matter. Assume that sets A and B have at most 10^4 elements each.
"""

def cartesian_product(A: set, B: set) -> set:
    """
    Returns the Cartesian product of two sets A and B as a set.
    
    Args:
        A (set): The first set.
        B (set): The second set.
    
    Returns:
        set: The Cartesian product of A and B.
    """
    
    cartesian_product_set = set()
    
    for a in A:
        for b in B:
            cartesian_product_set.add((a, b))
    
    return cartesian_product_set