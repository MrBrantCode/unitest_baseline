"""
QUESTION:
Create a function called `generate_parity` that takes a hexadecimal string as input and returns the binary representation of the input with an even parity bit appended to the end. The parity bit should be 0 if the total number of 1's in the binary representation is even, and 1 if it is odd. The input is guaranteed to be a hexadecimal string, and the output should be a binary string.
"""

# convert hexadecimal to binary and generate parity bit
def generate_parity(data):
    bin_value = bin(int(data, 16))[2:].zfill(4 * len(data))
    parity = '0' if bin_value.count('1') % 2 == 0 else '1'
    return bin_value + parity