"""
QUESTION:
## Task

Let's say we have a positive integer, `$n$`. You have to find the smallest possible positive integer that when multiplied by `$n$`, becomes a perfect power of integer `$k$`. A perfect power of `$k$` is any positive integer that can be represented as `$a^k$`. For example if `$k = 2$`, then `$36$` is a perfect power of `$k$`, but `$27$` isn't.

## Examples

```python
n, k = 100, 3  return  10, #because 10*100 becomes 1000, and 1000 = 10**3
n, k = 36, 2   return   1, #because 36 is already a perfect square 6**2
n, k = 72, 4   return  18, #because 18*72 = 1296 = 6**4
```

**Notes:** 
+ `$k, n \in \mathbb{N} $` and `$ 1 \lt n \lt 10^6,\text{ } 1 \lt k \lt 10 $`
+ However, the output may be way larger than `$10^6$`.

If you have trouble seeing the numbers, refresh your page ;-) Please rate this kata. All translations are welcome.

ABOVE: [If you see this:](https://imgur.com/TKY59S4), refresh your page.
"""

from collections import Counter
from math import ceil

PRIMES = [2] + [n for n in range(3, 1000, 2) if all((n % d for d in range(3, int(n ** 0.5) + 1, 2)))]

def get_factors(n):
    factors = []
    for p in PRIMES:
        if p > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return Counter(factors)

def find_smallest_multiplier(n, k):
    factors = get_factors(n)
    lcm = 1
    for p, e in factors.items():
        lcm *= p ** (ceil(e / k) * k)
    return lcm // n