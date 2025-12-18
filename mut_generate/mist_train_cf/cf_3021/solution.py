"""
QUESTION:
Implement a function `binary_to_hexadecimal(binary)` that takes a binary number as a string and returns its equivalent hexadecimal number as a string. The function should handle binary numbers of any length, work for both positive and negative binary numbers, and return the output in uppercase. The solution should not use built-in conversion functions or libraries, and its time complexity should be O(n), where n is the length of the input binary number.
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