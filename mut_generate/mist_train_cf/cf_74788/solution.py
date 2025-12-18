"""
QUESTION:
Write a function `ascii_to_binary` that takes a string of ASCII characters as input and returns the binary representation of the string's hexadecimal encoding without using any built-in binary conversion functions. The hexadecimal string should be converted to binary by mapping each hexadecimal digit to its corresponding 4-bit binary representation.
"""

def ascii_to_binary(ascii_str):
    """
    Convert an ASCII string to its binary representation.

    This function takes a string of ASCII characters as input, converts it into hexadecimal,
    and then maps each hexadecimal digit to its corresponding 4-bit binary representation.

    Args:
        ascii_str (str): The input ASCII string.

    Returns:
        str: The binary representation of the input string.
    """
    hex_to_bin = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "a": "1010", "b": "1011",
        "c": "1100", "d": "1101", "e": "1110", "f": "1111"
    }

    # Convert the ASCII string into hexadecimal
    hex_str = ascii_str.encode("utf-8").hex()

    # Encode the hexadecimal string into binary
    binary_str = "".join(hex_to_bin[i] for i in hex_str)

    return binary_str