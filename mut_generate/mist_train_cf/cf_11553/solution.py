"""
QUESTION:
Write a function `convert_to_base8(number)` that takes an integer `number` as input and returns its base 8 representation as a string. The function should handle both positive and negative integers.
"""

def convert_to_base8(number):
    if number == 0:
        return '0'
    
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)
    
    result = ''
    while number > 0:
        remainder = number % 8
        result = str(remainder) + result
        number = number // 8
    
    if is_negative:
        result = '-' + result
    
    return result