"""
QUESTION:
Write a function `total_rows(p, q, n, r, s)` that takes five parameters representing two fractions (p/q and r/s) and an integer n. The function should calculate the total number of rows in a blanket given that p/q represents the fraction of remaining rows to the total rows already knitted, and after knitting n more rows, the remaining rows become r/s of the total rows knitted. If the two input fractions are equal (considering reduced forms), the function should return a message stating they are the same.
"""

from fractions import Fraction

def total_rows(p, q, n, r, s):
    # Input fractions as strings with a '/' separator
    p_q = Fraction(p, q)
    r_s = Fraction(r, s)

    # If the fractions are the same, return a message
    if p_q == r_s:
        return "The input fractions are the same."

    rows_already_knitted = n / (p_q - r_s)
    total_rows = rows_already_knitted + rows_already_knitted * p_q
    
    return total_rows