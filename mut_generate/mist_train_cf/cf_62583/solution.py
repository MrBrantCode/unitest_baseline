"""
QUESTION:
Define a function 'array_gcd' that takes an integer array and returns the Greatest Common Divisor (GCD) of all integers in the array. The function should have an input array length between 1 and 10^3, and each integer 'a' in the array should be between 1 and 10^9.
"""

from typing import List
import math

def array_gcd(arr: List[int]) -> int:
    num1 = arr[0]
    num2 = arr[1]
    gcd = math.gcd(num1, num2)
  
    for i in range(2, len(arr)):
        gcd = math.gcd(gcd, arr[i])
  
    return gcd