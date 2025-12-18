"""
QUESTION:
Develop a function called 'array_lcm' that takes an integer array as input and returns their Least Common Multiple (LCM). The input array 'arr' will have a length between 1 and 10^3 (inclusive) and each integer 'a' within 'arr' will be between 1 and 10^9 (inclusive).
"""

import math
from typing import List

def array_lcm(arr: List[int]) -> int:
    """
    Utilize an optimal method to compute the Smallest Common Multiple (SCM)
    or Lowest Common Multiple (LCM) of an integer array.
    """
    
    def lcm(a: int, b: int) -> int:
        """
        Compute the LCM of two integers a and b.
        """
        return a * b // math.gcd(a, b)
                         
    
    lcm_value = arr[0]
    
    for num in arr[1:]:
        lcm_value = lcm(lcm_value, num)
    
    return lcm_value