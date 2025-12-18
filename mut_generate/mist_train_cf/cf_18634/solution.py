"""
QUESTION:
Create a function `decimal_to_hexadecimal(decimal)` that takes a decimal number as input and returns its corresponding hexadecimal value as a string. The function should handle negative decimal numbers and return an error message for invalid decimal inputs.
"""

def decimal_to_hexadecimal(decimal):
    # check if input is a valid decimal number
    try:
        decimal = int(decimal)
    except ValueError:
        return "Error: Invalid decimal number"

    # handle negative decimal numbers
    negative = False
    if decimal < 0:
        negative = True
        decimal = abs(decimal)

    # convert decimal to hexadecimal
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder + 55) + hexadecimal
        decimal = decimal // 16

    # add negative sign if applicable
    if negative:
        hexadecimal = "-" + hexadecimal

    return hexadecimal