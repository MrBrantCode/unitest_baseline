"""
QUESTION:
Write a function `binary_to_hex(binary)` that takes a binary string as input and returns its equivalent hexadecimal representation. The function must handle negative binary numbers, where the input string starts with a "-" sign. The function should not use any built-in functions or libraries for the conversion. It should be able to handle binary strings with lengths up to 10 million characters.
"""

def binary_to_hex(binary):
    if binary[0] == '-':
        return '-' + binary_to_hex(binary[1:])
    
    hexadecimal = ''
    power = len(binary) - 1
    
    hex_map = "0123456789ABCDEF"
    decimal = 0
    
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    
    while decimal > 0:
        hexadecimal = hex_map[decimal % 16] + hexadecimal
        decimal //= 16
    
    return hexadecimal if hexadecimal else '0'