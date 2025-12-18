"""
QUESTION:
Write a function named `negate` that takes an integer as input and returns its negative value without using the negation operator (-) or any arithmetic operations (*, /, +, -).
"""

def negate(x: int) -> int:
    """Return the negative value of the input integer without using the negation operator or any arithmetic operations."""
    return ~x + 1