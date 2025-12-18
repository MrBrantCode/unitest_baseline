"""
QUESTION:
Write a function `binary_to_hex(binary)` that takes a string of binary numbers as input and returns its hexadecimal equivalent without using built-in conversion functions. The input string may not have a length that is a multiple of 4, in which case it should be padded with leading zeros to make its length a multiple of 4. Each hexadecimal digit corresponds to a 4-digit binary number.
"""

def binary_to_hex(binary):
    hex_mapping = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }
    binary = binary.zfill(4 * ((len(binary) + 3) // 4))  # Make length multiple of 4
    hex_value = "".join(hex_mapping[binary[i:i+4]] for i in range(0, len(binary), 4))
    return hex_value