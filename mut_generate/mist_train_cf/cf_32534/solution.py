"""
QUESTION:
Implement a function to convert binary numbers to hexadecimal. The function should read binary numbers from the standard input, convert each to its hexadecimal representation, and print the result. The input binary numbers are provided line by line. The output should be a 2-digit hexadecimal representation of each input binary number.
"""

def binary_to_hex(binary):
    return "{0:02x}".format(int(binary, 2))