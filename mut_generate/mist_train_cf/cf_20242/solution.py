"""
QUESTION:
Convert a given integer to its equivalent hexadecimal value using recursion. Define a function `convertToHex(num)` that takes an integer `num` as input and returns its hexadecimal representation as a string. The function should use a recursive approach and a dictionary to map decimal values to their equivalent hexadecimal characters. The function should handle non-negative integers and return an empty string for input `0`.
"""

hex_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def entrance(num):
    hex_value = ''
    if num == 0:
        return hex_value
    remainder = num % 16
    hex_value = hex_map[remainder] + hex_value
    num = num // 16
    return entrance(num) + hex_value