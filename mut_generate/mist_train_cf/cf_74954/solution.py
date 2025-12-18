"""
QUESTION:
Create a function `convert_number` that takes two parameters: `number` and `conversion_type`. The function should convert a positive integer to its equivalent lowercase roman numeral or vice versa based on the `conversion_type` parameter. The `conversion_type` parameter can take two values: 'int_to_roman' or 'roman_to_int'. The integer input should be between 1 and 1000, and the roman numeral should align with its integer equivalent.

The function should include error-checking procedures to validate the input. If the input is invalid, it should return an error message. The function should handle cases where the roman numeral uses subtraction (e.g., IV for 4, IX for 9). 

Constraints:
- The integer input should be between 1 and 1000.
- The roman numeral should be in lowercase.
- The `conversion_type` parameter can only take 'int_to_roman' or 'roman_to_int' values.
"""

def convert_number(number, conversion_type):
    roman_to_int_mapping = {
        'i': 1, 'iv': 4, 'v': 5, 'ix': 9, 'x': 10, 'xl': 40, 'l': 50,
        'xc': 90, 'c': 100, 'cd': 400, 'd': 500, 'cm': 900, 'm': 1000
    }
    int_to_roman_mapping = {value: key for key, value in roman_to_int_mapping.items()}
    descending_values = sorted(int_to_roman_mapping.keys(), reverse=True)

    if conversion_type == 'int_to_roman':
        if not isinstance(number, int) or number < 1 or number > 1000:
            return 'Invalid number. Input should be an integer between 1 and 1000.'
        result = ''
        for value in descending_values:
            while number >= value:
                number -= value
                result += int_to_roman_mapping[value]
        return result.lower()
    elif conversion_type == 'roman_to_int':
        if not isinstance(number, str):
            return 'Invalid number. Input should be a string.'
        result = 0
        i = 0
        while i < len(number):
            if (i+1) < len(number) and number[i:i+2].lower() in roman_to_int_mapping:
                result += roman_to_int_mapping[number[i:i+2].lower()]
                i += 2
            elif number[i].lower() in roman_to_int_mapping:
                result += roman_to_int_mapping[number[i].lower()]
                i += 1
            else:
                return 'Invalid roman numeral.'
        return result
    else:
        return 'Invalid conversion_type. Options: int_to_roman or roman_to_int'