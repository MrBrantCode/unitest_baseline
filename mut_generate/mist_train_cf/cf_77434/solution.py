"""
QUESTION:
Write a function `geometric_mean(seq1, seq2)` that calculates the geometric mean of two sequences `seq1` and `seq2`, which may contain both integers and floats, as well as None values. The function should ignore None values, handle sequences of different lengths, and return None if both sequences are empty or only contain None values.
"""

from functools import reduce
from operator import mul
from math import pow

def geometric_mean(seq1, seq2):
    # Merge the sequences and exclude None values
    merged = [x for x in seq1 + seq2 if x is not None]
    
    # Compute the product of the numbers in the merged list
    product = reduce(mul, merged, 1)
    
    # Take the nth root of the product (where n is the length of the merged list)
    return pow(product, 1.0/len(merged)) if merged else None