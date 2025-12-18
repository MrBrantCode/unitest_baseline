"""
QUESTION:
Create a function `decimal_to_binary(decimal)` that converts a decimal number with a fractional part into an 8-bit binary representation. The binary representation should have the precision of its floating-point form and should be in the format of 'whole_part.binary_part'. The function should take a decimal number as input and return the corresponding binary representation as a string. Note: The output binary representation is not required to follow the IEEE 754 standard for floating-point numbers.
"""

def decimal_to_binary(decimal):
    if decimal >= 1:
        int_part = int(decimal)
        frac_part = decimal - int_part

        int_bin = []
        while int_part > 0:
            int_bin.append(str(int_part%2))
            int_part = int_part // 2

        frac_bin = []
        while frac_part > 0 and len(frac_bin) < 8:  # Limit to 8-bit binary representation
            frac_part *= 2
            bit = int(frac_part)
            if bit == 1:
                frac_part -= bit
                frac_bin.append('1')
            else:
                frac_bin.append('0')

        return "".join(int_bin[::-1]) + "." + "".join(frac_bin)
    else:
        return "Error: Input must be greater than 1"