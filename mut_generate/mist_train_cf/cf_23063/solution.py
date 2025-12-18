"""
QUESTION:
Implement a function `convert_number_system(number, from_base, to_base)` to convert a number from a given base to another base. The function should handle conversions between binary (base 2), octal (base 8), decimal (base 10), and hexadecimal (base 16) number systems. The input number should be less than or equal to 1000000 and the output number should be less than or equal to 1000000000.
"""

def convert_number_system(number, from_base, to_base):
    # Step 1: Convert to decimal
    decimal_number = int(str(number), from_base)

    # Step 2: Convert to the desired number system
    converted_number = oct(decimal_number)[2:] if to_base == 8 else (hex(decimal_number)[2:] if to_base == 16 else str(decimal_number))

    return converted_number