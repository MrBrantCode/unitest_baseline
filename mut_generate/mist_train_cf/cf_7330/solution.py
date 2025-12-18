"""
QUESTION:
Write a function `convert_and_sum` that takes an integer `decimal` as input and returns a dictionary containing the binary, hexadecimal, and octal representations of `decimal` as strings, as well as the sum of the digits in these representations. The input `decimal` is an integer between 0 and 511.
"""

def convert_and_sum(decimal):
    binary = bin(decimal)[2:]  
    hexadecimal = hex(decimal)[2:]  
    octal = oct(decimal)[2:]  

    binary_sum = sum(map(int, str(binary)))
    hexadecimal_sum = sum(int(digit, 16) for digit in hexadecimal)
    octal_sum = sum(int(digit, 8) for digit in octal)

    total_sum = binary_sum + hexadecimal_sum + octal_sum
    
    return {
        'binary': binary,
        'hexadecimal': hexadecimal,
        'octal': octal,
        'sum_of_digits': total_sum
    }