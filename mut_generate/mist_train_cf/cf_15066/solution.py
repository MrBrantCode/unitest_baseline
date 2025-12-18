"""
QUESTION:
Create a function `binary_to_roman` that takes a binary string as input, converts it to a decimal value, and returns its corresponding Roman numeral representation. The function should use a mapping of decimal values to Roman numerals, including the values for 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, and 1000, to construct the Roman numeral string.
"""

def binary_to_roman(binary_string):
    decimal_value = int(binary_string, 2)
    roman_mapping = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    
    roman_numeral = ''
    
    for value, numeral in roman_mapping.items():
        while decimal_value >= value:
            roman_numeral += numeral
            decimal_value -= value
    
    return roman_numeral