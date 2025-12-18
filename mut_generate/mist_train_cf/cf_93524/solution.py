"""
QUESTION:
Implement a function called "decimal_to_octal" that takes an integer (positive or negative) as input and returns its octal equivalent as a string, without using built-in functions or libraries for decimal to octal conversion.
"""

def decimal_to_octal(number):
    if number == 0:
        return "0"
    
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)
    
    octal_digits = []
    while number > 0:
        octal_digits.insert(0, str(number % 8))
        number = number // 8
    
    octal_number = ''.join(octal_digits)
    if is_negative:
        octal_number = "-" + octal_number
    
    return octal_number