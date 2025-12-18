"""
QUESTION:
Create a function named `splitIgnoringCommas` that takes a string as input. The string contains values separated by commas, but some values are enclosed in quotes and may also contain commas. The function should split the input string into a list of values, ignoring commas within quoted sections. The function should handle both quoted and unquoted values correctly and return the resulting list.
"""

def split_ignoring_commas(input_string):
    result = []
    current_value = ''
    in_quotes = False

    for char in input_string:
        if char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            result.append(current_value)
            current_value = ''
        else:
            current_value += char

    if current_value:
        result.append(current_value)

    return result