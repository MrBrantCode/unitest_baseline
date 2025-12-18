"""
QUESTION:
Write a function called `extract_roman_numerals` that takes two parameters: `text` and optionally `start` and `end`. This function should extract all numerical figures written in Roman numerals from `text`, convert them to decimal numbers, and return them in a list. The function should be able to handle both whole numbers and fractions, as well as different variations of Roman numerals. If `start` and `end` are provided, the function should only return numbers within the specified range.
"""

import re

def roman_to_decimal(s):
    roman_to_decimal = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
        'I': 1
    }

    decimal = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in roman_to_decimal:
            decimal += roman_to_decimal[s[i:i+2]]
            i += 2
        else:
            decimal += roman_to_decimal[s[i]]
            i += 1

    return decimal

def extract_roman_numerals(text, start=None, end=None):
    roman_pattern = r'\b(?=[MDCLXVI])(M?D?C?L?X?V?I{0,3})(XC|XL|IX|IV|CM|CD)?\b'
    fraction_pattern = r'\b(?=[MDCLXVI])(M?D?C?L?X?V?I{0,3})(XC|XL|IX|IV|CM|CD)?(\/)(?=[MDCLXVI])(M?D?C?L?X?V?I{0,3})(XC|XL|IX|IV|CM|CD)?\b'

    roman_numerals = re.findall(roman_pattern, text)
    fractions = re.findall(fraction_pattern, text)

    extracted_numbers = []
    for numeral in roman_numerals:
        value = roman_to_decimal(numeral[0] + numeral[1])
        extracted_numbers.append(value)

    for fraction in fractions:
        numerator = roman_to_decimal(fraction[0] + fraction[1])
        denominator = roman_to_decimal(fraction[3] + fraction[4])
        value = float(numerator) / float(denominator)
        extracted_numbers.append(value)

    if start is not None and end is not None:
        extracted_numbers = [n for n in extracted_numbers if n >= start and n <= end]
    elif start is not None:
        extracted_numbers = [n for n in extracted_numbers if n >= start]
    elif end is not None:
        extracted_numbers = [n for n in extracted_numbers if n <= end]

    return extracted_numbers