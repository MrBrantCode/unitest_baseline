"""
QUESTION:
Implement a function binary_to_hexadecimal(binary) that takes a binary number as a string and returns its equivalent hexadecimal number as a string. The input binary number is always valid and the output hexadecimal number should be in uppercase. The function should not use any built-in conversion functions or libraries and should work for binary numbers of any length, including those representing negative numbers in two's complement form.
"""

def binary_to_hexadecimal(binary):
    lookupTable = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    while len(binary) % 4 != 0:
        binary = "0" + binary

    hexadecimal = ""
    for i in range(0, len(binary), 4):
        group = binary[i:i+4]
        hexadecimal += lookupTable[group]

    return hexadecimal