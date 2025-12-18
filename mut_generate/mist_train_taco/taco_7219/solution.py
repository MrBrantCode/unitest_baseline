"""
QUESTION:
German mathematician Christian Goldbach (1690-1764) [conjectured](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture) that every even number greater than 2 can be represented by the sum of two prime numbers. For example, `10` can be represented as `3+7` or `5+5`.

Your job is to make the function return a list containing all unique possible representations of `n` in an increasing order if `n` is an even integer; if `n` is odd, return an empty list. Hence, the first addend must always be less than or equal to the second to avoid duplicates.

Constraints : `2 < n < 32000` and `n` is even


## Examples
```
26  -->  ['3+23', '7+19', '13+13']

100 -->  ['3+97', '11+89', '17+83', '29+71', '41+59', '47+53']

7   -->  [] 
```
"""

import math

def goldbach_partitions(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    
    if n % 2 != 0:
        return []
    
    partitions = []
    for first in range(2, n // 2 + 1):
        if is_prime(first):
            second = n - first
            if is_prime(second):
                partitions.append(f"{first}+{second}")
    
    return partitions