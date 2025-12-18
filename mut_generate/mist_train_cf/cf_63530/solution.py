"""
QUESTION:
You are given a function `fractionToDecimal` that takes an integer `numerator` and an integer `denominator` as input. The function should return a string representing the decimal representation of the fraction `numerator/denominator`. If the decimal representation is repeating, the function should return the repeating decimal representation as a string. The function should handle division by zero errors and potential underflow errors.
"""

def fractionToDecimal(numerator, denominator):
    if not numerator: return "0"
    result = ""
    if (numerator > 0) ^ (denominator > 0):
        result += "-"
    numerator, denominator = abs(numerator), abs(denominator)
    result += str(numerator // denominator)
    remainder = numerator % denominator
    if not remainder: 
        return result
    result += "."
    d = {}
    while remainder:
        if remainder in d:
            result = result[:d[remainder]] + "(" + result[d[remainder]:] + ")"
            break
        d[remainder] = len(result)
        remainder *= 10
        result += str(remainder // denominator)
        remainder %= denominator
    return result