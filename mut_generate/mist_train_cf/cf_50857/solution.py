"""
QUESTION:
Write a function `convert_to_number` that takes a string as input, extracts the numeric characters (including optional decimal point and negative sign), and returns the corresponding number (either integer or float). The function should ignore non-numeric characters and return `None` if no numeric characters are found in the input string. The function should also handle edge cases where the string contains multiple decimal points or negative signs in invalid positions.
"""

def convert_to_number(string):
    number = ""
    dot_count = 0 # to ensure only one '.' is in the numeric string
    for char in string:
        if char == '.' and dot_count == 0: 
            number += char
            dot_count += 1
        elif char.isdigit():
            number += char
        elif (char == '-') and (number == ''): # to ensure '-' only at the start
            number += char
    # Check if the resultant string can be converted to int or float, else return None
    try:
        return int(number) if '.' not in number else float(number)
    except ValueError:
        return None