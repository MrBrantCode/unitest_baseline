"""
QUESTION:
Ayrat has number n, represented as it's prime factorization p_{i} of size m, i.e. n = p_1·p_2·...·p_{m}. Ayrat got secret information that that the product of all divisors of n taken modulo 10^9 + 7 is the password to the secret data base. Now he wants to calculate this value.


-----Input-----

The first line of the input contains a single integer m (1 ≤ m ≤ 200 000) — the number of primes in factorization of n. 

The second line contains m primes numbers p_{i} (2 ≤ p_{i} ≤ 200 000).


-----Output-----

Print one integer — the product of all divisors of n modulo 10^9 + 7.


-----Examples-----
Input
2
2 3

Output
36

Input
3
2 3 2

Output
1728



-----Note-----

In the first sample n = 2·3 = 6. The divisors of 6 are 1, 2, 3 and 6, their product is equal to 1·2·3·6 = 36.

In the second sample 2·3·2 = 12. The divisors of 12 are 1, 2, 3, 4, 6 and 12. 1·2·3·4·6·12 = 1728.
"""

from functools import reduce

def calculate_divisor_product(m: int, primes: list[int]) -> int:
    p = 10 ** 9 + 7
    D = {}
    
    for prime in primes:
        if prime in D:
            D[prime] += 1
        else:
            D[prime] = 1
    
    prod = reduce(lambda x, y: x * y % p, primes)
    deg = reduce(lambda x, y: x * y, (d + 1 for d in D.values()))
    
    if deg % 2:
        prod = reduce(lambda x, y: x * y % p, (pow(d, i // 2, p) for (d, i) in D.items()))
        ans = pow(prod, deg % (p - 1), p)
    else:
        ans = pow(prod, deg // 2 % (p - 1), p)
    
    return ans