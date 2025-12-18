"""
QUESTION:
Create a function named `reverse_digits` that takes a single number as input and returns a list of its reversed digits. The function should handle both positive and negative integers and floating-point numbers. The returned list should include the decimal point (if present) and the negative sign (if present). The function should preserve the relative order of the decimal point and negative sign.
"""

def reverse_digits(number):
    number_str = str(number)
    if number < 0:
        number_str = number_str[1:] # remove the negative sign
        reversed_str = number_str[::-1] # reverse the string
        reversed_str = '-' + reversed_str # add the negative sign back
    else:
        reversed_str = number_str[::-1] # reverse the string
    
    reversed_digits = []
    for char in reversed_str:
        reversed_digits.append(char)
    
    return reversed_digits