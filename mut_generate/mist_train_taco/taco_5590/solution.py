"""
QUESTION:
Define a "prime prime" number to be a rational number written as one prime number over another prime number: `primeA / primeB` (e.g. `7/31`)

Given a whole number `N`, generate the number of "prime prime" rational numbers less than 1, using only prime numbers between `0` and `N` (non inclusive).

Return the count of these "prime primes", and the integer part  of their sum.

## Example

```python
N = 6

# The "prime primes" less than 1 are:
2/3, 2/5, 3/5               # count: 3

2/3 + 2/5 + 3/5 = 1.6667    # integer part: 1

Thus, the function should return 3 and 1.
```
"""

from bisect import bisect_left

def sieve(n):
    (sieve, primes) = ([0] * (n + 1), [])
    for i in range(2, n + 1):
        if not sieve[i]:
            primes.append(i)
            for j in range(i ** 2, n + 1, i):
                sieve[j] = 1
    return primes

PRIMES = sieve(100000)

def count_prime_primes_and_sum(N):
    lst = PRIMES[:bisect_left(PRIMES, N)]
    divs = [p / q for (i, p) in enumerate(lst) for q in lst[i + 1:]]
    return (len(divs), int(sum(divs)))