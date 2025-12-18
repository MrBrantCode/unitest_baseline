"""
QUESTION:
Create a function called `decimal_equivalent` to take two integers, `numerator` and `denominator`, representing a fraction and calculate its decimal equivalent. If the decimal representation is a repeating decimal, return the decimal equivalent as a string and identify the repeating sequence of digits. Restriction: assume the denominator is non-zero.
"""

def decimal_equivalent(numerator, denominator):
    integer_part = numerator // denominator
    remainder = numerator % denominator
    decimal_part = ""
    remainders = {}
    
    while remainder != 0 and remainder not in remainders:
        remainders[remainder] = len(decimal_part)
        remainder *= 10
        decimal_part += str(remainder // denominator)
        remainder %= denominator
    
    if remainder != 0:
        start = remainders[remainder]
        decimal_part = decimal_part[:start] + "(" + decimal_part[start:] + ")"
    
    return str(integer_part) + "." + decimal_part