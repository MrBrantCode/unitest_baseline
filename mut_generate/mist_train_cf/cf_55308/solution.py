"""
QUESTION:
Write a function 'array_gcd' that calculates the Greatest Common Divisor (GCD) of an array of integers. The function should take an array of integers as input and return their GCD. The array will contain between 1 and 10^3 integers, each in the range 1 to 10^9.
"""

import math
from typing import List

def array_gcd(arr: List[int]) -> int:
    num1 = arr[0]
    num2 = arr[1]
    gcd = math.gcd(num1, num2)

    for i in range(2, len(arr)):
        gcd = math.gcd(gcd, arr[i])
    
    return gcd