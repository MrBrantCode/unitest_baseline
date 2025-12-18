"""
QUESTION:
Create a function named `reverse_digits` that takes a number as input and returns a list of its digits in reverse order. The function should handle negative numbers by prepending the negative sign to the reversed digits, and it should also handle floating-point numbers by including the decimal point in the reversed digits.
"""

def reverse_digits(number):
    number_str = str(number)
    if number < 0:
        number_str = number_str[1:] 
        reversed_str = number_str[::-1] 
        reversed_str = '-' + reversed_str 
    else:
        reversed_str = number_str[::-1] 
    
    reversed_digits = []
    for char in reversed_str:
        reversed_digits.append(char)
    
    return reversed_digits