"""
QUESTION:
Implement a function `convert_number` that takes two parameters: `number` and `conversion_type`. The `number` parameter should be a positive integer (1-1000) or a lowercase roman numeral, and `conversion_type` should be either 'int_to_roman' or 'roman_to_int'. The function should convert the input `number` from integer to roman numeral or vice versa based on the `conversion_type`. The output should be a string for 'int_to_roman' conversion and an integer for 'roman_to_int' conversion.
"""

def convert_number(number, conversion_type):
    roman_to_int_map = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    int_to_roman_map = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}

    if conversion_type == 'int_to_roman':
        result = ''
        num = number
        for value in sorted(int_to_roman_map.keys(), reverse=True):
            while num >= value:
                result += int_to_roman_map[value]
                num -= value
        return result
    elif conversion_type == 'roman_to_int':
        num = 0
        prev_value = 0
        for ch in number[::-1]:
            value = roman_to_int_map[ch]
            if value >= prev_value:
                num += value
            else:
                num -= value
            prev_value = value
        return num