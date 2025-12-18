"""
QUESTION:
Write a recursive function `int_to_string` that takes an integer `num` as input and returns its string representation. The function should handle both positive and negative integers.
"""

def int_to_string(num):
    result = ""
    
    if num == 0:
        result += '0'
        return result
    
    if num < 0:
        result += '-'
        num = abs(num)
    
    digits = num
    count = 0
    while digits != 0:
        digits //= 10
        count += 1
    
    power = 10**(count-1)
    first_digit = num // power
    result += chr(first_digit + ord('0'))
    
    num %= power
    
    if num != 0:
        result += int_to_string(num)
    
    return result