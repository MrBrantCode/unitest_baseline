"""
QUESTION:
The aim of the kata is to decompose `n!` (factorial n) into its prime factors.

Examples:
```
n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.

n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"

n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
```

Prime numbers should be in increasing order. When the exponent of a prime is 1 don't put the exponent.

Notes

- the function is `decomp(n)` and should return the decomposition of `n!` into its prime factors in increasing order of the primes, as a string.
- factorial can be a very big number (`4000! has 12674 digits`, n will go from 300 to 4000).
- In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use `dynamically allocated character strings`.
"""

from collections import defaultdict

def prime_factorization_of_factorial(n):
    def prime_factors(num):
        factors = defaultdict(int)
        i = 2
        while num > 1:
            while num % i == 0:
                num //= i
                factors[i] += 1
            i += 1
        return factors

    factor_counts = defaultdict(int)
    for i in range(2, n + 1):
        for key, value in prime_factors(i).items():
            factor_counts[key] += value

    return ' * '.join(
        f'{x}^{y}' if y > 1 else str(x)
        for x, y in sorted(factor_counts.items())
    )