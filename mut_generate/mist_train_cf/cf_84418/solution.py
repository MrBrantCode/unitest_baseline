"""
QUESTION:
Create a function 'array_gcd' that calculates the Second GCD for an array of integers. The Second GCD is the greatest integer that divides at least two different pairs of numbers in the array. The function must utilize the most computationally efficient method. The input array will have a length between 4 and 10^3 (inclusive), and each integer in the array will be between 1 and 10^9 (inclusive).
"""

from typing import List
from math import gcd
from heapq import nlargest

def second_gcd(arr: List[int]) -> int:
    gcd_vals = set(gcd(arr[i], arr[j]) for i in range(len(arr)) for j in range(i+1, len(arr)))
    return nlargest(2, gcd_vals)[-1]