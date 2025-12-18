"""
QUESTION:
Create two functions, `get_lcm(nums)` and `get_gcd(nums)`, that can calculate the Least Common Multiple (LCM) and the Greatest Common Divisor (GCD) of n numbers, respectively. The input `nums` can be a list containing integers and/or lists of integers. The functions should be able to handle nested lists of integers and return the LCM and GCD as integers.
"""

from typing import List, Union
from functools import reduce
import math

def get_lcm(nums: List[Union[int, List[int]]]) -> int:
    flat_nums = [i for n in nums for i in (n if isinstance(n, list) else (n,))]
    return reduce(lambda x, y: x * y // math.gcd(x, y), flat_nums)

def get_gcd(nums: List[Union[int, List[int]]]) -> int:
    flat_nums = [i for n in nums for i in (n if isinstance(n, list) else (n,))]
    return reduce(math.gcd, flat_nums)