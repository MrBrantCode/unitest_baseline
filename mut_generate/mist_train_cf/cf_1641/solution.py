"""
QUESTION:
Write a function `convert_number` that converts a string to a number (either integer or floating-point). The string can contain scientific notation, negative numbers, and commas as thousand separators. The function should remove leading and trailing white spaces, ignore commas, and raise an exception if the input string contains non-numeric characters other than the allowed ones. The function should handle edge cases such as extremely large or small numbers.
"""

def convert_number(string):
    # Remove leading and trailing white spaces
    string = string.strip()

    # Remove commas from the string
    string = string.replace(",", "")

    # Check if the string starts with a negative sign
    is_negative = False
    if string.startswith("-"):
        is_negative = True
        string = string[1:]

    # Check if the string contains scientific notation
    if "e" in string:
        # Split the string into the base number and the exponent
        base, exponent = string.split("e")
        base = float(base)
        exponent = int(exponent)
        result = base * (10 ** exponent)
    else:
        result = float(string)

    # If the original string started with a negative sign, negate the result
    if is_negative:
        result = -result

    return result