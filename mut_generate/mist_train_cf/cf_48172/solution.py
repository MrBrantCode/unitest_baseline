"""
QUESTION:
Create a function named `custom_binary_to_octal` that takes a string of binary digits as input and returns its octal representation as a string. The function should not use any built-in or imported functions for conversion. The input string should be validated to ensure it only contains '0' and '1' characters. If the input string is invalid, the function should return an error message. The function should handle binary strings that start with one or more '0's by padding them with leading zeroes to a multiple of 3 in length before conversion.
"""

def custom_binary_to_octal(y: str):
    if not all(c in '01' for c in y):
        return "Invalid binary input"
        
    while len(y) % 3 != 0:
        y = '0' + y
        
    result = ''
    for i in range(0, len(y), 3):
        octal_digit = int(y[i]) * 4 + int(y[i+1]) * 2 + int(y[i+2])
        result += str(octal_digit)
        
    while result[0] == '0' and len(result) > 1:
        result = result[1:]

    return result