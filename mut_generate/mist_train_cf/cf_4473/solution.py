"""
QUESTION:
Compute the sum of elements in two arrays using a function named `computeSum` with a time complexity less than O(n^2). The function takes two arrays `a` and `b` of size `n` as input and returns the sum of all elements.
"""

def computeSum(a, b, n):
    """
    Compute the sum of elements in two arrays.

    Args:
    a (list): The first array.
    b (list): The second array.
    n (int): The size of the arrays.

    Returns:
    int: The sum of all elements in both arrays.
    """
    total_sum = 0
    for i in range(n):
        total_sum += a[i]
        total_sum += b[i]
    return total_sum