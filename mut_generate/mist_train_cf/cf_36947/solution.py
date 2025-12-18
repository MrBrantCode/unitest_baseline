"""
QUESTION:
Create a function `int_to_roman(num)` that takes an integer `num` between 1 and 3999 as input and returns its Roman numeral representation. The function should follow the standard rules of Roman numeral representation, where smaller symbols can be placed before larger symbols to denote subtraction.
"""

def int_to_roman(num):
    tbl = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }
    res = ''
    for k in sorted(tbl.keys(), reverse=True):
        while num >= k:
            res += tbl[k]
            num -= k
    return res