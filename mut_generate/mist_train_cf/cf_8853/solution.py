"""
QUESTION:
Write a function named `convert_to_roman` that takes an array of hexadecimal strings as input, converts each string to its equivalent Roman numeral, and returns an array of the converted values. The function should handle both uppercase and lowercase hexadecimal characters and should not use any built-in functions or libraries for conversion.
"""

def convert_to_roman(hex_strings):
    decimal_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'A': 10, 'b': 11, 'B': 11, 'c': 12, 'C': 12,
        'd': 13, 'D': 13, 'e': 14, 'E': 14, 'f': 15, 'F': 15
    }

    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    def hex_to_decimal(hex_string):
        decimal = 0
        for i, char in enumerate(hex_string[::-1]):
            decimal += decimal_map[char] * (16 ** i)
        return decimal

    def decimal_to_roman(decimal):
        roman = ''
        for value, numeral in roman_numerals.items():
            while decimal >= value:
                roman += numeral
                decimal -= value
        return roman

    result = []
    for hex_string in hex_strings:
        decimal = hex_to_decimal(hex_string)
        roman = decimal_to_roman(decimal)
        result.append(roman)
    return result