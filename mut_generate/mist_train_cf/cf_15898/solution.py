"""
QUESTION:
Write a function called `decimal_to_binary(decimal)` that takes an integer `decimal` as input and returns its binary representation as a string. The function should handle negative decimal numbers by returning their two's complement binary representation. The time complexity should be O(log n) and space complexity should be O(log n), where n is the given decimal number.
"""

def decimal_to_binary(decimal):
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