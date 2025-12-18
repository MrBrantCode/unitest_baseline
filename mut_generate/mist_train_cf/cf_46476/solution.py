"""
QUESTION:
Write a function `fraction` that takes a string `decimal` representing a decimal number and returns a fraction in the format of two integers representing the `numerator` and `denominator`. The function should handle both recurring and non-recurring decimal numbers. The length of the input string is guaranteed to be less than 104. The output `numerator` and `denominator` should be in the range of `-2^31 <= numerator, denominator <= 2^31 - 1` and `denominator != 0`.
"""

def fraction(decimal):
    import fractions

    if '(' in decimal:
        integer, decimal = decimal.split('.')
        non_recurring, recurring = decimal[:-1].split('(')
        numerator = int(integer + non_recurring + recurring) - int(integer + non_recurring)
        denominator = int('9'*len(recurring) + '0'*len(non_recurring))
    else:
        integer, decimal = decimal.split('.') if '.' in decimal else (decimal, '0')    
        numerator = int(integer + decimal)
        denominator = 10**len(decimal)
    
    result = fractions.Fraction(numerator, denominator)
    return result.numerator, result.denominator