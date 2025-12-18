"""
QUESTION:
Implement a function named `convert_number_system` that takes three parameters: `num` (the number to be converted), `from_base` (the base of the input number), and `to_base` (the base of the output number). The function should convert `num` from `from_base` to `to_base`. The input number `num` should not exceed 1000000, the output number should not exceed 1000000000, and the number of digits in `num` should not exceed 10. The function should handle conversions between binary (base 2), octal (base 8), decimal (base 10), and hexadecimal (base 16) number systems.
"""

def convert_number_system(num, from_base, to_base):
    # Convert num from from_base to decimal
    decimal = int(str(num), from_base)
    
    # Convert decimal to to_base
    convert_string = "0123456789ABCDEF"
    if decimal == 0:
        return '0'
    result = ''
    while decimal > 0:
        remainder = decimal % to_base
        result = convert_string[remainder] + result
        decimal = decimal // to_base

    return result