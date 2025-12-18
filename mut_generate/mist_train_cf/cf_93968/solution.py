"""
QUESTION:
Write a function `decimal_to_binary(decimal)` that converts a given decimal number into its binary form, including handling negative decimal numbers and returning their two's complement binary representation. The function should have a time complexity of O(log n) and a space complexity of O(log n), where n is the given decimal number.
"""

def entance(decimal):
    if decimal == 0:
        return '0'

    is_negative = False
    if decimal < 0:
        is_negative = True
        decimal = abs(decimal)

    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

    if is_negative:
        binary = complement(binary)

    return binary

def complement(binary):
    complemented = ''
    for bit in binary:
        if bit == '0':
            complemented += '1'
        else:
            complemented += '0'

    carry = 1
    result = ''
    for bit in complemented[::-1]:
        if carry == 0:
            result = bit + result
        else:
            if bit == '0':
                result = '1' + result
                carry = 0
            else:
                result = '0' + result

    return result