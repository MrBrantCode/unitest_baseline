"""
QUESTION:
*This is the advanced version of the [Total Primes](https://www.codewars.com/kata/total-primes/) kata.*

---

The number `23` is the smallest prime that can be "cut" into **multiple** primes: `2, 3`. Another such prime is `6173`, which can be cut into `61, 73` or `617, 3` or `61, 7, 3` (all primes). A third one is `557` which can be sliced into `5, 5, 7`. Let's call these numbers **total primes**.

Notes:
* one-digit primes are excluded by definition;
* leading zeros are also excluded: e.g. splitting `307` into `3, 07` is **not** valid


## Task

Complete the function that takes a range `[a..b]` (both limits included) and returns the total primes within that range (`a ≤ total primes ≤ b`).

The tests go up to 10^(6).
~~~if:python
For your convenience, a list of primes up to 10^(6) is preloaded, called `PRIMES`.
~~~


## Examples
```
(0, 100)  ==>  [23, 37, 53, 73]

(500, 600) ==> [523, 541, 547, 557, 571, 577, 593]
```
Happy coding!

---

## My other katas

If you enjoyed this kata then please try [my other katas](https://www.codewars.com/collections/katas-created-by-anter69)! :-)

#### *Translations are welcome!*
"""

import numpy as np
from itertools import accumulate

def sieve_primes(n):
    sieve = np.ones(n // 2, dtype=np.bool)
    limit = 1 + int(n ** 0.5)
    for a in range(3, limit, 2):
        if sieve[a // 2]:
            sieve[a * a // 2::a] = False
    prime_indexes = 2 * np.nonzero(sieve)[0].astype(int) + 1
    prime_indexes[0] = 2
    return set(map(str, prime_indexes))

PRIMES = sieve_primes(10 ** 6)

def all_primes(s):
    if int(s) < 10:
        return s in PRIMES
    for n in accumulate(s[:-1]):
        if n in PRIMES:
            m = s[len(n):]
            if m in PRIMES or all_primes(m):
                return True
    return False

def find_total_primes_in_range(a, b):
    return [int(num) for num in map(str, range(max(10, a), b + 1)) if num in PRIMES and all_primes(num)]