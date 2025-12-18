"""
QUESTION:
Write a function called `highest_common_factor` that takes an array of integers as input and returns their highest common factor. The function should work for arrays of any length.
"""

import math
def highest_common_factor(arr):
    num1 = arr[0]
    num2 = arr[1]
    hcf = math.gcd(num1, num2)

    for i in range(2, len(arr)):
        hcf = math.gcd(hcf, arr[i])
        
    return hcf