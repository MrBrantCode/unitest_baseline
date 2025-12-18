"""
QUESTION:
Write a function `convert_to_base_16(num)` that takes a float number as input and returns its equivalent hexadecimal representation as a string. The function should handle negative numbers, special numbers such as infinity and NaN, and edge cases such as zero and negative zero.
"""

def convert_to_base_16(num):
    """
    Convert a float number from base 10 to base 16.
    """
    # Handle edge cases such as zero and negative zero
    if num == 0:
        return '0'

    # Handle special cases such as infinity and NaN
    if num == float('inf'):
        return 'inf'
    if num == float('-inf'):
        return '-inf'
    if num != num:
        return 'NaN'

    # Convert the whole number part to base 16
    whole_part = abs(int(num))
    whole_base_16 = hex(whole_part)[2:]  # remove '0x' from the hexadecimal representation

    # Convert the fractional part to base 16
    fractional_part = abs(num - whole_part)
    fractional_base_16 = ''

    # Handle decimal numbers
    if fractional_part != 0:
        # Multiply the fractional part by 16 until it becomes zero or reaches desired precision
        while fractional_part > 0:
            fractional_part *= 16
            digit = int(fractional_part)
            fractional_base_16 += hex(digit)[2:]
            fractional_part -= digit

    # Handle negative numbers
    if num < 0:
        return '-' + whole_base_16 + '.' + fractional_base_16
    else:
        return whole_base_16 + '.' + fractional_base_16