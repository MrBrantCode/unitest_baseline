"""
QUESTION:
Write a recursive function `octal_to_binary` that takes an integer `octal` as input and returns its binary representation as a string.
"""

def octal_to_binary(octal):
    # Base case: if the octal number is 0, return an empty string
    if octal == 0:
        return ""
    
    # Recursive case: divide the octal number by 8 (octal to decimal) and then by 2 
    # and append the remainder to the result
    return octal_to_binary(octal // 8) + octal_to_binary(octal % 8 // 2) + str(octal % 2)