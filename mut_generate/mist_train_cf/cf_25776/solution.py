"""
QUESTION:
Write a function named 'last_k_digits' that takes two integers 'base' and 'exponent' and an integer 'k' as input, and returns the last k digits of base raised to the power of exponent as an integer. The function should work for large inputs and the result should be returned without leading zeros.
"""

def last_k_digits(base, exponent, k):
    """
    This function calculates the last k digits of base raised to the power of exponent.

    Args:
    base (int): The base number.
    exponent (int): The exponent to which the base is raised.
    k (int): The number of digits to return from the result.

    Returns:
    int: The last k digits of base raised to the power of exponent.
    """
    # Calculate the power and take the modulus of 10^k to get the last k digits
    result = pow(base, exponent, 10**k)
    # Convert the result to string, remove leading zeros and convert back to integer
    return int(str(result).lstrip('0') or '0')