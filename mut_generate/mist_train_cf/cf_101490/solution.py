"""
QUESTION:
Write a function "valor" that evaluates a polynomial p(x) given a list of coefficients p and a value x. The function should be able to handle large coefficients and should use an efficient algorithm for polynomial evaluation. The function should take in two parameters: p, a list of coefficients where p[i] is the coefficient of x^i, and x, the value at which to evaluate the polynomial. The function should return the value of the polynomial p(x). The function should support polynomials of any degree and should be able to handle extremely large coefficients without overflowing.
"""

def valor(p, x):
    """
    Evaluates a polynomial p(x) given a list of coefficients p and a value x.
    
    Args:
    p (list): A list of coefficients where p[i] is the coefficient of x^i.
    x (int): The value at which to evaluate the polynomial.
    
    Returns:
    int: The value of the polynomial p(x).
    """
    n = len(p)
    result = p[n-1]
    for i in range(n-2, -1, -1):
        result = result * x + p[i]
    return result