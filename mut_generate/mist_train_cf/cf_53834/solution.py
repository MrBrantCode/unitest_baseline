"""
QUESTION:
Create a function `find_recurring_numbers` that takes a list of fractions as input and returns a dictionary of fractions with their corresponding recurring decimal numbers. Each fraction should be represented as a string in the format 'numerator/denominator'. The function should consider recurring decimals up to 9 repeating digits and a maximum precision of 100 decimal places.
"""

import decimal

def find_recurring_numbers(fractions):
    recurring = {}
    
    for fraction in fractions:
        numerator, denominator = map(int, fraction.split('/'))
        decimal.getcontext().prec = 100
        dec = decimal.Decimal(numerator) / decimal.Decimal(denominator)
        dec_str = str(dec)
        if '.' in dec_str:
            dec_str = dec_str.split('.')[1]
            for i in range(1, 10):
                if i > len(dec_str):
                    break
                for j in range(len(dec_str) - i + 1):
                    substr = dec_str[j:j+i]
                    if substr == dec_str[j+i:j+2*i] and substr != i*'0':
                        recurring[fraction] = substr
                        break
                if fraction in recurring:
                    break
                    
    return recurring