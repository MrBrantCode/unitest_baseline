"""
QUESTION:
Create a function `hex_to_bin(hex_list)` that takes a list of hexadecimal numbers as input, converts valid hexadecimal numbers to binary and returns two lists. The first list should contain the binary equivalents of the valid hexadecimal numbers, and the second list should contain error messages for the invalid hexadecimal numbers. The error messages should be formatted as "Error: Invalid hexadecimal number {hex_num}". If a hexadecimal number is invalid, it should be skipped and not included in the binary output.
"""

def hex_to_bin(hex_list):
    bin_list = []
    error_list = []
    for i in hex_list:
        try:
            bin_list.append(bin(int(i, 16))[2:].zfill(4))
        except ValueError:
            error_list.append(f"Error: Invalid hexadecimal number {i}")
    return bin_list, error_list