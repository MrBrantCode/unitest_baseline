"""
QUESTION:
Write a function `count_equal_elements` that takes two tensors `A` and `B`, both with a dimension of `(2*x, 1)`, and returns the number of identical elements in the last `x` elements of both tensors.
"""

def count_equal_elements(A, B, x):
    """
    This function takes two tensors A and B, both with a dimension of (2*x, 1), 
    and returns the number of identical elements in the last x elements of both tensors.

    Parameters:
    A (tensor): The first tensor with a dimension of (2*x, 1)
    B (tensor): The second tensor with a dimension of (2*x, 1)
    x (int): The number of elements to compare from the end of both tensors

    Returns:
    int: The number of identical elements in the last x elements of both tensors
    """
    return sum(A[-x:] == B[-x:])