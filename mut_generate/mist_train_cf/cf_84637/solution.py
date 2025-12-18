"""
QUESTION:
Create a function `gcd_array` that calculates the Greatest Common Divisor (GCD) of an array of integers. The function should accept an array of integers and return their GCD using a high-performance algorithm. The array will contain between 1 and 10^3 integers, each between 1 and 10^6.
"""

from typing import List

def gcd_array(numerals: List[int]) -> int:
    def gcd(a: int, b: int) -> int:
        return a if b == 0 else gcd(b, a % b)

    g = numerals[0]
    for n in numerals[1:]:
        g = gcd(g, n)

    return g