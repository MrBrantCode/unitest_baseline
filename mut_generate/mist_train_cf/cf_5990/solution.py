"""
QUESTION:
Write a function named `roman_to_decimal` that takes a Roman numeral string as input and returns its decimal equivalent. The function should handle Roman numerals with subtractive notation (e.g., IV for 4, IX for 9, etc.) and repeating numerals up to three times in a row (e.g., III for 3, XXII for 22, etc.). The function should also handle cases where subtractive notation is combined with repeating numerals.
"""

def roman_to_decimal(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_num = 0
    for i in range(len(roman_numeral)):
        if i > 0 and roman_dict[roman_numeral[i]] > roman_dict[roman_numeral[i-1]]:
            decimal_num += roman_dict[roman_numeral[i]] - 2 * roman_dict[roman_numeral[i-1]]
        else:
            decimal_num += roman_dict[roman_numeral[i]]
    return decimal_num