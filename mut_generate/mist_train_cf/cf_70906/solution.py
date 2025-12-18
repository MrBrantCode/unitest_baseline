"""
QUESTION:
Create a function named `number_to_binary` that takes two parameters: a string `x` representing a number and an integer `base` representing the base of the number. The function should convert the input number into its binary equivalent and support base 8 (octal), base 10 (decimal), base 16 (hexadecimal), and base 2 (binary). The function should also handle negative numbers and non-integer numbers.
"""

def number_to_binary(x: str, base: int):
    """
    Convert an input number, represented as a string, of a specified base (integer) into its binary equivalent. 
    Also handle the conversion of negative numbers and non-integer numbers into their binary equivalents. 
    The function should support base 8 (octal), base 10 (decimal),  base 16 (hexadecimal), and base 2 (binary).
    """
    
    if x[0] == '-':
        prefix = '-'
        x = x[1:]
    else:
        prefix = ''
    
    if '.' in x:
        integer_part, fractional_part = x.split('.')
        
        integer_part = int(integer_part, base)
        fractional_part = int(fractional_part, base) / (base ** len(fractional_part))
        
        binary_integer_part = bin(integer_part)[2:]
        binary_fractional_part = '.'
        
        while fractional_part > 0:
            fractional_part *= 2
            bit = int(fractional_part)
            
            if bit == 1:
                fractional_part -= bit
                binary_fractional_part += '1'
            else:
                binary_fractional_part += '0'
                
        return prefix + binary_integer_part + binary_fractional_part
    else:
        return prefix + bin(int(x, base))[2:]