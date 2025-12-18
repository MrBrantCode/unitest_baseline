"""
QUESTION:
Implement a function called "decimal_to_octal" that takes a decimal number as input and returns its octal equivalent. The function should handle both positive and negative numbers, as well as decimal numbers with fractional parts. If the decimal number has a fractional part, round the octal equivalent to 2 decimal places. Do not use any built-in functions or libraries for converting decimal to octal.
"""

def decimal_to_octal(decimal):
    # Check if the number is negative
    is_negative = False
    if decimal < 0:
        is_negative = True
        decimal = abs(decimal)

    # Split the number into integer and fractional parts
    integer_part = int(decimal)
    fractional_part = decimal - integer_part

    # Convert the integer part to octal
    octal_integer = ""
    while integer_part > 0:
        remainder = integer_part % 8
        octal_integer = str(remainder) + octal_integer
        integer_part = integer_part // 8

    # Convert the fractional part to octal
    octal_fractional = ""
    while fractional_part > 0 and len(octal_fractional) < 2:
        fractional_part *= 8
        digit = int(fractional_part)
        octal_fractional += str(digit)
        fractional_part -= digit

    # Combine the integer and fractional parts
    octal = octal_integer + "." + octal_fractional

    # Add the negative sign if necessary
    if is_negative:
        octal = "-" + octal

    return octal