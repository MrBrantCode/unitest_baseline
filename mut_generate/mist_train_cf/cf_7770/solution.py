"""
QUESTION:
Implement a function named `generate_squares` that takes an integer `n` as input and returns an array of size `n`, where each element at index `i` is the square of `i`. If `n` is negative or zero, the function should return an empty array. The function should not use any built-in mathematical functions or operators for exponentiation or multiplication. The time complexity of the algorithm should be O(n) or less.
"""

def generate_squares(n):
    """
    Returns an array of size n, where each element at index i is the square of i.
    If n is negative or zero, an empty array is returned.
    
    Time complexity: O(n)
    """
    if n <= 0:
        return []
    
    squares = [i * i for i in range(n)]
    return squares