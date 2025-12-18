"""
QUESTION:
Create a function `G(N)` that calculates the sum of the values of `g(n)` for `n` ranging from 1 to `N`, where `g(n)` is the sum of `(-1)^i * gcd(n, i^2)` for `i` ranging from 1 to `n`. The function should be able to handle large values of `N`, like `12345678`.
"""

def G(N):
    """
    Calculate the sum of the values of g(n) for n ranging from 1 to N.
    
    Parameters:
    N (int): The upper limit of the range.
    
    Returns:
    int: The sum of the values of g(n) for n ranging from 1 to N.
    """
    # Calculate the sum of squares of first N natural numbers
    sum_sq_n = N*(N+1)*(2*N+1)//6 
    
    # Calculate the sum of first N natural numbers
    sum_n = N 
    
    # Calculate G(N) by subtracting the sum of first N natural numbers from the sum of squares
    return sum_sq_n - sum_n