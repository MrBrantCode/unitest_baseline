"""
QUESTION:
Write the function `euclideanGcd(a: int, b: int, c: int, d: int, e: int, f: int)` that calculates the Greatest Common Divisor (GCD) of six positive integers using the Euclidean Algorithm method. 

Constraints:
- 1 <= a, b, c, d, e, f <= 10^9
- The numbers may not be distinct (duplicates allowed)
- If two or more numbers are zero, consider the first non-zero number encountered during GCD computation
- If all numbers are zero, return "Invalid input"

The function should achieve a time complexity of O(log n).
"""

def euclideanGcd(a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    """
    This function calculates the Greatest Common Divisor (GCD) of six positive integers using the Euclidean Algorithm method.

    Args:
    a (int): First positive integer.
    b (int): Second positive integer.
    c (int): Third positive integer.
    d (int): Fourth positive integer.
    e (int): Fifth positive integer.
    f (int): Sixth positive integer.

    Returns:
    int: The greatest common divisor of the six input integers.
    """

    def gcd(x: int, y: int) -> int:
        """Helper function to calculate the GCD of two numbers."""
        while y:
            x, y = y, x % y
        return x

    # Check if all numbers are zero
    if not any((a, b, c, d, e, f)):
        return "Invalid input"

    # Calculate the GCD of all numbers
    result = a
    for num in (b, c, d, e, f):
        if num:
            result = gcd(result, num)

    return result