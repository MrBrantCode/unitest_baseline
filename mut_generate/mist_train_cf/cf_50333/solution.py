"""
QUESTION:
Create a function named `primesInRange` that takes two parameters `startnum` and `endnum` and returns a list of all prime numbers within the range from `startnum` to `endnum` (inclusive) along with the count of prime numbers. The function should only consider integers and should not include negative numbers. The input range should be within the limit of the programming language's integer data type. The function should be efficient and optimized for large ranges.
"""

import math

def primesInRange(startnum, endnum):
    primes = []
    for num in range(startnum, endnum+1):
        if num > 1: 
            for i in range(2, int(math.sqrt(num)) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes, len(primes)