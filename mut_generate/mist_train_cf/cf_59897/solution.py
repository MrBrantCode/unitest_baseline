"""
QUESTION:
Implement a function named `binaryToOctal` that takes a binary string as input and returns its octal equivalent as a string. The function should not use any built-in or imported libraries for conversion. It must handle cases where the binary string begins with more than one 0 by adding leading zeroes until its length is a multiple of 3. The function should also include error-checking to handle cases where the input string is not a valid binary number. If the input string is invalid, the function should return "Error: Invalid binary number".
"""

def binaryToOctal(binary: str):
    while len(binary) % 3 != 0:
        binary = "0" + binary      # Add leading zeroes until the binary number is a multiple of 3

    binary = [binary[i:i+3] for i in range(0, len(binary), 3)]    # Split the binary number into groups of 3

    octal = ""
    for b in binary:
        if b == "000":
            octal += "0"
        elif b == "001":
            octal += "1"
        elif b == "010":
            octal += "2"
        elif b == "011":
            octal += "3"
        elif b == "100":
            octal += "4"
        elif b == "101":
            octal += "5"
        elif b == "110":
            octal += "6"
        elif b == "111":
            octal += "7"
        else:
            return "Error: Invalid binary number"    # Error-checking if the input is not a binary number

    return octal.lstrip("0") or "0"    # Removing leading zeroes 