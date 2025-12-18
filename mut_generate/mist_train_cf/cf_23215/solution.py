"""
QUESTION:
Create a function `convert_hex_to_roman(hex_bank)` that takes an array of hexadecimal strings `hex_bank` as input and returns a string of Roman numerals. The function should convert each hexadecimal string in `hex_bank` to its corresponding decimal value, then convert the decimal value to a Roman numeral. The function should return a single string containing all the Roman numerals concatenated together.
"""

def convert_hex_to_roman(hex_bank):
    lookup_table = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    roman_table = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    decimal_bank = []
    for hex_string in hex_bank:
        decimal = 0
        for digit in hex_string:
            decimal = decimal * 16 + lookup_table[digit]
        decimal_bank.append(decimal)

    roman_numeral = ''
    for decimal in decimal_bank:
        for value in sorted(roman_table.keys(), reverse=True):
            while decimal >= value:
                roman_numeral += roman_table[value]
                decimal -= value

    return roman_numeral