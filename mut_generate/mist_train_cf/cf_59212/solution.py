"""
QUESTION:
Write a function `binary_to_unicode(bin_code)` that takes a string of binary digits as input, converts it into its corresponding Unicode symbol, and returns the symbol. If the input binary code is invalid, the function should return an error message.
"""

def binary_to_unicode(bin_code):
    try:
        unicode_value = int(bin_code, 2) # Convert binary to decimal
        char = chr(unicode_value)  # Convert decimal to character
        return char
    except Exception as e:
        return "Invalid binary code: {}".format(e)