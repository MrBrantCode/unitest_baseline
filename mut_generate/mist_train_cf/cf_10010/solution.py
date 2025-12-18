"""
QUESTION:
Write a function named `roman_product` that takes two Roman numerals as input and returns their product as a Roman numeral. The function should handle Roman numerals from 1 to 3999 and follow the standard rules of Roman numerals where a smaller numeral placed before a larger one means subtraction. The function should not take any other input types and should not perform any error checking for invalid inputs.
"""

def roman_to_decimal(numeral):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    prev_value = 0

    for symbol in reversed(numeral):
        value = roman_map[symbol]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
            prev_value = value

    return decimal

def decimal_to_roman(decimal):
    roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    roman = ""

    for value, symbol in sorted(roman_map.items(), reverse=True):
        while decimal >= value:
            roman += symbol
            decimal -= value

    return roman

def roman_product(num1, num2):
    decimal1 = roman_to_decimal(num1)
    decimal2 = roman_to_decimal(num2)
    product_decimal = decimal1 * decimal2
    product_roman = decimal_to_roman(product_decimal)
    
    return product_roman