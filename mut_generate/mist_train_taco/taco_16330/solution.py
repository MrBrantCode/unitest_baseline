"""
QUESTION:
In this Kata you must convert integers numbers from and to a negative-base binary system.

Negative-base systems can accommodate all the same numbers as standard place-value systems, but both positive and negative numbers are represented without the use of a minus sign (or, in computer representation, a sign bit); this advantage is countered by an increased complexity of arithmetic operations.

To help understand, the first eight digits (in decimal) of the Base(-2) system is: 

`[1, -2, 4, -8, 16, -32, 64, -128]`


Example conversions:

`Decimal, negabinary`
```
6,   '11010'
-6,  '1110'
4,   '100'
18,  '10110'
-11, '110101'
```
"""

def convert_negabinary(value, from_base, to_base):
    if from_base == 'decimal' and to_base == 'negabinary':
        # Convert decimal to negabinary
        ds = []
        i = int(value)
        while i != 0:
            ds.append(i & 1)
            i = -(i >> 1)
        return ''.join((str(d) for d in reversed(ds))) if ds else '0'
    
    elif from_base == 'negabinary' and to_base == 'decimal':
        # Convert negabinary to decimal
        i = 0
        for c in str(value):
            i = -(i << 1) + int(c)
        return i
    
    else:
        raise ValueError("Invalid base conversion. Supported bases are 'decimal' and 'negabinary'.")