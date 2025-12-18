"""
QUESTION:
Create a function `convert_to_base16` that takes a positive integer `number` as input and returns its base 16 representation as a string. Note that the input number is in base 10.
"""

def convert_to_base16(number):
    result = ""
    while number > 0:
        remainder = number % 16
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('a') + remainder - 10) + result
        number = number // 16
    return result