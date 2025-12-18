"""
QUESTION:
Create a function named `convert_bin` that takes a list of binary numerals as input and outputs their decimal and hexadecimal representations. The function should handle large binary numerals (signed/unsigned) and validate if the entered numeral is a valid binary. If the numeral is not valid, output an error message. The function should not assume any specific length or range of the input binary numerals.
"""

def convert_bin(binaries):
    def validate_bin(binary):
        try:
            int(binary, 2)
            return True
        except ValueError:
            return False

    def bin_to_dec(binary):
        return int(binary, 2)

    def bin_to_hex(binary):
        return hex(int(binary, 2))[2:]

    for binary in binaries:
        if validate_bin(binary):
            return {"Binary": binary, "Decimal": bin_to_dec(binary), "Hexadecimal": bin_to_hex(binary)}
        else:
            return f"{binary} is not a valid binary numeral!"