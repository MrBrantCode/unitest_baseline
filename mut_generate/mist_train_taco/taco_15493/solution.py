"""
QUESTION:
Write a program which finds the greatest common divisor of two natural numbers a and b

Hint

You can use the following observation:

For integers x and y, if x ≥ y, then gcd(x, y) = gcd(y, x%y)

Constrants

1 ≤ a, b ≤ 109

Input

a and b are given in a line sparated by a single space.

Output

Output the greatest common divisor of a and b.

Examples

Input

54 20


Output

2


Input

147 105


Output

21
"""

def find_gcd(a: int, b: int) -> int:
    """
    Finds the greatest common divisor (GCD) of two natural numbers a and b.

    Parameters:
    a (int): The first natural number.
    b (int): The second natural number.

    Returns:
    int: The greatest common divisor of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a