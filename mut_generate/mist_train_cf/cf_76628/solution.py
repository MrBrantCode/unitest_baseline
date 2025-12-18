"""
QUESTION:
Write a function `conjugate_multiplication(c1, c2)` that takes two complex numbers `c1` and `c2` as input and returns the result of their conjugate multiplication. The function should return the product of the conjugates of `c1` and `c2`, not the conjugate of their product.
"""

def conjugate_multiplication(c1, c2):
    """
    This function takes two complex numbers c1 and c2 as input and returns the result of
    their conjugate multiplication.
    """
    return (c1.conjugate() * c2.conjugate())