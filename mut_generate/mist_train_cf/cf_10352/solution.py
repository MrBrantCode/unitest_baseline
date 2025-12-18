"""
QUESTION:
Implement the `multiply` function to multiply two big integers `x` and `y`, handling negative numbers and returning the result modulo a given number `mod`. The function should be able to handle arbitrarily large integers.
"""

def multiply(x, y, mod):
    """
    Multiplies two big integers x and y, handling negative numbers and returning the result modulo mod.

    Args:
        x (int): The first big integer.
        y (int): The second big integer.
        mod (int): The modulo number.

    Returns:
        int: The result of multiplying x and y modulo mod.
    """
    x = abs(x)
    y = abs(y)

    result = x * y

    return result % mod