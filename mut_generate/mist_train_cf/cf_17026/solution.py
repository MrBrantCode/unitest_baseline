"""
QUESTION:
Implement a function named `multiply` that takes three parameters: two big integers `x` and `y`, and a modulo number `mod`. The function should multiply `x` and `y`, handle negative numbers, and return the result modulo `mod`. The function must use bitwise operators instead of arithmetic operators to perform the multiplication. The input integers can be arbitrarily large.
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
    if x < 0:
        x *= -1
        sign_x = -1
    else:
        sign_x = 1

    if y < 0:
        y *= -1
        sign_y = -1
    else:
        sign_y = 1

    result = 0
    while y:
        if y & 1:
            result = (result + x) % mod
        x = (x << 1) % mod
        y >>= 1

    return result * sign_x * sign_y % mod