"""
QUESTION:
Write a function `calculate_max_value(n)` and `to_hex(n)` where `n` is a positive integer. The `calculate_max_value(n)` function should calculate the maximum value that can be contained in N-bit binary data manually (without using built-in functions to calculate powers of 2). The `to_hex(n)` function should convert the calculated decimal number to hexadecimal notation. The input `n` can be any positive integer. The output should be the maximum value in decimal and its equivalent hexadecimal notation.
"""

def calculate_max_value(n):
    max_value = 0
    current_power = 1
    for _ in range(n):
        max_value += current_power
        current_power *= 2
    return max_value

def to_hex(n):
    hex_digits = '0123456789ABCDEF'
    if n < 16:
        return hex_digits[n]
    else:
        div, mod = divmod(n, 16)
        return to_hex(div) + hex_digits[mod]