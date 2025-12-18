"""
QUESTION:
Create a function named `custom_binary_to_octal` that takes a string of binary digits as input and returns its octal equivalent as a string. The function must not use any built-in or external libraries for conversion. It should handle cases where the binary string starts with more than one '0', is empty, or contains characters other than '0' or '1'. If the input string is invalid, the function should return an error message.
"""

def custom_binary_to_octal(y: str):
    """Convert a binary input (string) to its octal representation (string) without using any built-in or imported functions"""
    
    while len(y) > 1 and y[0] == '0':
        y = y[1:]
    
    if len(y) == 0 or any(c not in '01' for c in y):
        return 'Error: Invalid binary string'
    
    digits = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
    
    while len(y) % 3 != 0:
        y = '0' + y
    
    return ''.join(digits[y[i:i+3]] for i in range(0, len(y), 3))