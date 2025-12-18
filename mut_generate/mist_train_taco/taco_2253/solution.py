"""
QUESTION:
Write a function that reverses the bits in an integer.

For example, the number `417` is `110100001` in binary. Reversing the binary is `100001011` which is `267`.

You can assume that the number is not negative.
"""

def reverse_bits(n: int) -> int:
    """
    Reverses the bits in the given non-negative integer.

    Parameters:
    n (int): The non-negative integer whose bits are to be reversed.

    Returns:
    int: The integer obtained by reversing the bits of the input integer.
    """
    return int(bin(n)[:1:-1], 2)