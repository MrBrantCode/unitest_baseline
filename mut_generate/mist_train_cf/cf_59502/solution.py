"""
QUESTION:
Implement the `mul_0_997` function, which takes a 16-bit unsigned integer as input and returns the result of multiplying it by approximately 0.997. The function should use the least possible number of instructions. The microcontroller uses 16-bit integers and 32-bit long integers, and does not support floating-point operations.
"""

def mul_0_997(input: int) -> int:
    """
    Multiply a 16-bit unsigned integer by approximately 0.997.

    This function uses a fixed-point representation to achieve the multiplication,
    as the microcontroller does not support floating-point operations.

    :param input: 16-bit unsigned integer
    :return: Result of multiplying the input by approximately 0.997
    """
    scale_factor = 1024
    factor = 1020
    temp = input * factor
    return temp // scale_factor