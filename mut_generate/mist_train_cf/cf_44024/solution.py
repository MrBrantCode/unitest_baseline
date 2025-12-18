"""
QUESTION:
Write a function `hex_calc(n)`, `binary_calc(n)`, and `octal_calc(n)` that calculates the hexadecimal, binary, and octal representations of a given positive integer `n` respectively. The functions should handle large numbers efficiently. The output should be a string prefixed with '0x' for hexadecimal, '0b' for binary, and '0o' for octal. The functions should also handle the case when `n` is 0.
"""

def hex_calc(n):
    if n == 0:
        return '0x0'
    hex_num = ''
    hex_values = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    while n > 0:
        reminder = n % 16
        if reminder in hex_values:
            rem_str = hex_values[reminder]
        else:
            rem_str = str(reminder)
        hex_num = rem_str + hex_num
        n = n // 16
    return '0x' + hex_num

def binary_calc(n):
    if n == 0:
        return '0b0'
    binary_num = ''
    while n > 0:
        binary_num = str(n % 2) + binary_num
        n = n // 2
    return '0b' + binary_num

def octal_calc(n):
    if n == 0:
        return '0o0'
    octal_num = ''
    while n > 0:
        octal_num = str(n % 8) + octal_num
        n = n // 8
    return '0o' + octal_num