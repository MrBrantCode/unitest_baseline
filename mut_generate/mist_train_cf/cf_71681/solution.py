"""
QUESTION:
Write a function `modify_abs_values_v3(lst, n)` that takes a list of numerical values `lst` and a positive integer `n` between 2 and 100 as input. The function should return the multiplication result of the absolute values of these numbers, factoring in only their closest rounded-down integers, excluding the elements that are divisible by any prime number less than or equal to `n`. If `n` is not in the specified range, the function should return -1. The function should handle exceptions/errors without crashing and should be able to handle large numbers and arrays efficiently, with a reduced time complexity.
"""

from math import isqrt
from itertools import compress, count

def modify_abs_values_v3(lst, n):
    if n < 2 or n > 100:
        return -1

    primes = list(compress(count(), bytearray([(i%2 != 0) for i in range(n + 1)])))
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n-x)//2+1,2):
            primes[(x*y)//2] = False
    primes = [2] + [2 * x + 1 for x in compress(range((n + 1) // 2), primes)]

    result = 1
    for num in lst:
        value = int(abs(num))
        if value != 0 and all(value % p for p in primes):
            result *= value

    return result