"""
QUESTION:
Write a function `gcd_array` that takes an integer `n` and a 2D list of integers `numbers` as input, where each sublist contains an array of integers. The function should calculate the Greatest Common Divisor (GCD) of each array and return a list of these GCDs.

Constraints: 
1 <= n <= 500, 
1 <= len(array) <= 10^5, 
1 <= array[i] <= 10^9.
"""

import math
from typing import List

def gcd_array(n: int, numbers: List[List[int]]) -> List[int]:
    result = []
    for number in numbers:
        gcd = number[0]
        for i in range(1, len(number)):
            gcd = math.gcd(gcd, number[i])
        result.append(gcd)
    return result