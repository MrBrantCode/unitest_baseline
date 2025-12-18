"""
QUESTION:
Create a function `convert_number` that takes a string as input, converts it to a number (either integer or float), and returns the result. The string can contain integers, floating-point numbers, scientific notation, negative numbers, commas as thousand separators, and leading/trailing white spaces. The function should remove commas, handle scientific notation, and raise an exception if the input string contains non-numeric characters other than allowed ones.
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