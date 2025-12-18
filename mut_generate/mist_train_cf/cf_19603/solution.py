"""
QUESTION:
Write a function `convert_string_to_integer` that takes a string as input and returns the corresponding integer value. The string can be a decimal or hexadecimal number, and it can have leading/trailing whitespace and/or a negative sign. If the string starts with "0x" or "0X", it is interpreted as a hexadecimal number. The function should handle these different cases correctly and return the integer value of the input string.
"""

def convert_string_to_integer(string):
    # Remove leading/trailing whitespace
    string = string.strip()
    
    # Check for negative number
    negative = False
    if string[0] == "-":
        negative = True
        string = string[1:]
    
    # Check for hexadecimal representation
    hexadecimal = False
    if string.startswith("0x") or string.startswith("0X"):
        hexadecimal = True
        string = string[2:]
    
    # Convert string to integer
    if hexadecimal:
        result = int(string, 16)
    else:
        result = int(string, 10)
    
    # Apply negative sign if necessary
    if negative:
        result *= -1
    
    return result