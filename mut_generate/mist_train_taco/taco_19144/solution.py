"""
QUESTION:
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:


Input: numerator = 1, denominator = 2
Output: "0.5"


Example 2:


Input: numerator = 2, denominator = 1
Output: "2"

Example 3:


Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""

def fraction_to_decimal(numerator: int, denominator: int) -> str:
    if numerator * denominator < 0:
        add_negative = True
    else:
        add_negative = False
    
    numerator, denominator = abs(numerator), abs(denominator)
    integer_part = numerator // denominator
    new_numerator = numerator - integer_part * denominator
    
    if new_numerator == 0:
        result = str(integer_part)
        if add_negative:
            return '-' + result
        else:
            return result
    
    dict_residuals = {}
    digit_location = 0
    digit_array = []
    residual = new_numerator
    is_repeating = False
    
    while True:
        new_digit, residual = single_digit(residual, denominator)
        digit_location += 1
        
        if residual == 0:
            digit_array.append(str(new_digit))
            break
        elif residual in dict_residuals:
            digit_array.append(str(new_digit))
            is_repeating = True
            break
        else:
            dict_residuals[residual] = digit_location
            digit_array.append(str(new_digit))
    
    if is_repeating:
        loc = dict_residuals[residual]
        result = f"{integer_part}.{''.join(digit_array[:loc])}({''.join(digit_array[loc:])})"
    else:
        result = f"{integer_part}.{''.join(digit_array)}"
    
    if add_negative:
        return '-' + result
    else:
        return result

def single_digit(value: int, denominator: int) -> tuple[int, int]:
    return (int(10 * value // denominator), 10 * value % denominator)