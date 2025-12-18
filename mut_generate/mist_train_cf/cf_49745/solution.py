"""
QUESTION:
Write a function named `int_to_roman` that converts an integer into its Roman numeral representation. The function should take one integer argument and return a string. The function should work for any integer from 1 to 3999.
"""

def int_to_roman(input):
    # validate that input is a number
    if type(input) != type(1):
        return False

    # define roman numerals
    roman_nums = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 
                  50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    result_str = ''
 
    # convert number to roman numerals
    for key in sorted(roman_nums.keys(), reverse=True):
        while input >= key:
            result_str += roman_nums[key]
            input -= key
 
    return result_str