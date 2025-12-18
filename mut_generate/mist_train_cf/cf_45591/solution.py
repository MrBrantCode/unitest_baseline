"""
QUESTION:
Find a function `find_exponent(input)` that takes a numerical input and determines if it can be expressed as a power of another number. If so, the function should return the base and the exponent; otherwise, it should return `None`. The solution should not use brute force and should achieve a time complexity of O(log n) or better. The input is a single integer value.
"""

from math import sqrt, log2

def find_exponent(input):
    for base in range(2, int(sqrt(input))+1): 
        exponent = log2(input) / log2(base)  
        while exponent >= 2: 
            if base ** round(exponent) == input:
                return base, int(round(exponent))
            exponent -= 1
    return None