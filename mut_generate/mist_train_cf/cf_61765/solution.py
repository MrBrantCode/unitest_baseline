"""
QUESTION:
Compute the function S(n, m), which represents the sum of all integers in a sequence after m iterations, where the sequence starts with integers from 2 to n and each iteration involves dividing each integer by its smallest prime factor and appending the product of these factors. The result should be returned modulo 1234567891.
"""

def S(n, m):
    """
    Compute the sum of all integers in a sequence after m iterations.
    
    The sequence starts with integers from 2 to n and each iteration involves 
    dividing each integer by its smallest prime factor and appending the product 
    of these factors. The result is returned modulo 1234567891.
    
    Args:
        n (int): The upper limit of the initial sequence.
        m (int): The number of iterations.
    
    Returns:
        int: The sum of all integers in the sequence after m iterations.
    """
    return ((m * (n * (n + 1)) // 2) % 1234567891)