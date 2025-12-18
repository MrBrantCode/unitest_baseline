"""
QUESTION:
Write a function `int_to_32bit_binary(n)` that converts an integer `n` to a 32-bit binary string. The most significant bit represents the sign of the number (1 for negative, 0 for positive). The function should not use any built-in functions or libraries that directly convert integers to binary. If the binary representation has fewer than 32 bits, add leading zeros to make it 32 bits long.
"""

def int_to_32bit_binary(n):
    if n < 0:
        sign_bit = '1'
    else:
        sign_bit = '0'

    # Taking the absolute value of n
    n = abs(n)

    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n = n // 2

    # Reversing the list
    binary.reverse()

    # Adding leading zeros if needed
    if len(binary) < 31:
        binary = ['0'] * (31 - len(binary)) + binary

    # Adding the sign bit
    binary.insert(0, sign_bit)

    # Joining the list elements into a single string
    binary_string = ''.join(binary)

    return binary_string