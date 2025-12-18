"""
QUESTION:
Create a function named `decimal_to_hexadecimal` that takes an integer decimal number as input and prints both its decimal and hexadecimal representations. The function should handle decimal numbers up to 1000, display an error message for any number outside this range (-1000 to 1000), and convert negative decimal numbers to their sign-magnitude hexadecimal representation.
"""

def decimal_to_hexadecimal(decimal):
    if decimal < -1000 or decimal > 1000:
        print("Error: Decimal number must be between -1000 and 1000")
        return

    if decimal < 0:
        decimal = abs(decimal)
        sign = "-"
    else:
        sign = ""

    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal //= 16

    if hexadecimal == "":
        hexadecimal = "0"

    print("Decimal:", sign + str(decimal))
    print("Hexadecimal:", sign + hexadecimal)