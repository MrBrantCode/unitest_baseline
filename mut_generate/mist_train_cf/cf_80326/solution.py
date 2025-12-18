"""
QUESTION:
Write a function `square_rooting_and_conversion(n, l, base, precision, complexity)` that calculates either square root or root of a list of numbers from `n` to `n+l` (inclusive) and converts the results into a specified base system (up to hexadecimal) with the given precision. The function should return a list of strings representing the converted numbers. The base system should be specified by `base` and the precision by `precision`. The `complexity` parameter should be either "squareroot" or "root", where "root" means the l-th root.

Restrictions:

*   The function should return -1 if `n` is less than 1, `base` is not between 2 and 16 (inclusive), or `precision` is less than 0.
*   The function should return -1 if `complexity` is "root" and `l` is less than 1.
*   The function should handle the integer and fractional parts of the numbers separately during the base conversion.
"""

import math

def square_rooting_and_conversion(n, l, base, precision, complexity):
    if n < 1 or base < 2 or base > 16 or precision < 0:
        return -1
    
    numbers = list(range(n, n+l+1))
    result = []

    if complexity == "squareroot":
        operations = [math.sqrt(num) for num in numbers]
        
    elif complexity == "root":
        if l < 1:
            return -1
        
        operations = [math.pow(num, 1/l) for num in numbers]
            
    else:
        return -1

    def decimal_to_base(num, base):
        chars = "0123456789ABCDEF"
        
        if num < base:
            return chars[num]
        
        else:
            return decimal_to_base(num // base, base) + chars[num % base]

    def fraction_to_base_n(num, base, precision):
        chars = "0123456789ABCDEF"
        
        result = ""
        
        for _ in range(precision):
            num = num * base
            digit = int(num)
            result += chars[digit]
            num -= digit
        
        return result

    for operation in operations:
        decimal = round(operation, precision)
        integer_part, fraction_part = str(decimal).split('.')

        integer_part = int(integer_part)
        fraction_part = int(fraction_part) / (10 ** len(str(fraction_part)))

        integer_part = decimal_to_base(integer_part, base)
        fraction_part = fraction_to_base_n(fraction_part, base, precision)

        result.append("0b" + str(integer_part) + "." + str(fraction_part))

    return result