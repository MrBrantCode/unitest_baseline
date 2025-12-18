"""
QUESTION:
Create a function `convert_to_roman` that converts a positive integer less than 4000 to a Roman Numeral in uppercase letters. If the input is not a positive integer less than 4000, the function should return an error message.
"""

def convert_to_roman(num):
    if not isinstance(num, int) or num <= 0 or num >= 4000:
        return "Error: Invalid input. Please enter a positive integer less than 4000."
    
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    
    result = ''
    
    for value, symbol in roman_numerals.items():
        while num >= value:
            result += symbol
            num -= value
    
    return result