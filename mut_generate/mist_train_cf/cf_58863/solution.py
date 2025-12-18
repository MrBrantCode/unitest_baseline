"""
QUESTION:
Determine whether the sum of the 8-bit representations of the integers 109 and -42 falls within the feasible range for each of the following numeric representations: One's complement, Two's complement, and Sign and magnitude. Implement a function to calculate and return the result using Two's complement representation, given that the range for an 8-bit number is from -128 to 127.
"""

def twos_complement_sum(a, b, bits):
    """
    Calculate the sum of two integers in Two's complement representation.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        bits (int): The number of bits for the representation.

    Returns:
        int: The sum of a and b in Two's complement representation.
    """

    # Convert to binary representation
    binary1 = bin(a % (1 << bits))[2:].zfill(bits)
    binary2 = bin(b & ((1 << bits) - 1))[2:].zfill(bits)

    # Add the binary representations
    res = bin(int(binary1, 2) + int(binary2, 2))[2:]

    # Discard overflow, if any
    res = res[-bits:]

    # Calculate decimal value
    res = -int(res, 2) if res[0] == '1' else int(res, 2)

    return res