"""
QUESTION:
Implement the `decimal_to_octal` function, which takes an integer `n` as input and returns a string representing the octal equivalent of the input number. The function should not use any built-in functions for decimal to octal conversion.
"""

def decimal_to_octal(n):
    if n == 0:
        return '0'
    octal_digits = []
    while n > 0:
        remainder = n % 8
        octal_digits.append(str(remainder))
        n = n // 8
    octal_digits.reverse()
    return ''.join(octal_digits)