"""
QUESTION:
Write a function `has_unit_root` that takes as input a lag polynomial `p` and returns `True` if it has a unit root and `False` otherwise. The function should be able to handle polynomials of any degree, but for simplicity, you can assume the input polynomial is a list of coefficients in descending order of powers, i.e., `[a_n, a_{n-1}, ..., a_1, a_0]`, where `p(x) = a_n x^n + a_{n-1} x^{n-1} + ... + a_1 x + a_0`.
"""

def has_unit_root(p):
    """
    Checks if a polynomial has a unit root.

    Args:
    p (list): A list of coefficients in descending order of powers.

    Returns:
    bool: True if the polynomial has a unit root, False otherwise.
    """
    return p[0] == 1 and all(coeff == 0 for coeff in p[1:])