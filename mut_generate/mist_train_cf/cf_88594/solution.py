"""
QUESTION:
Write a function `convert_base(number, base, target_base)` that takes in a positive integer `number` and two bases `base` and `target_base` in the range of 2 to 36. The function should convert the given `number` from `base` to `target_base` and return the converted number as a string, without using any built-in functions or libraries that directly solve the problem, and with a time complexity of O(logN), where N is the given number.
"""

def entrance(number, base, target_base):
    if number == 0:
        return '0'
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    converted_number = ''
    
    while number > 0:
        remainder = number % target_base
        converted_number = digits[remainder] + converted_number
        number //= target_base
    
    return converted_number