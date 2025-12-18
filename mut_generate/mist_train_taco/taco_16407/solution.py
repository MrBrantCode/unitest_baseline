"""
QUESTION:
Dima loves representing an odd number as the sum of multiple primes, and Lisa loves it when there are at most three primes. Help them to represent the given number as the sum of at most than three primes.

More formally, you are given an odd numer n. Find a set of numbers p_{i} (1 ≤ i ≤ k), such that



 1 ≤ k ≤ 3

 p_{i} is a prime

 $\sum_{i = 1}^{k} p_{i} = n$

The numbers p_{i} do not necessarily have to be distinct. It is guaranteed that at least one possible solution exists.


-----Input-----

The single line contains an odd number n (3 ≤ n < 10^9).


-----Output-----

In the first line print k (1 ≤ k ≤ 3), showing how many numbers are in the representation you found.

In the second line print numbers p_{i} in any order. If there are multiple possible solutions, you can print any of them.


-----Examples-----
Input
27

Output
3
5 11 11



-----Note-----

A prime is an integer strictly larger than one that is divisible only by one and by itself.
"""

def represent_odd_as_sum_of_primes(n: int) -> tuple:
    """
    Represent the given odd number n as the sum of at most three primes.

    Parameters:
    n (int): An odd number (3 ≤ n < 10^9).

    Returns:
    tuple: A tuple containing the number of primes k (1 ≤ k ≤ 3) and a list of primes p_i.
    """
    limit = int(n ** 0.5) + 1
    lim12 = max(limit, 12)
    lim = lim12 // 6
    l = [False, True, True] * lim
    lim = lim * 3 - 1
    for (i, s) in enumerate(l):
        if s:
            (p, pp) = (i * 2 + 3, (i + 3) * i * 2 + 3)
            le = (lim - pp) // p + 1
            if le > 0:
                l[pp::p] = [False] * le
            else:
                break
    l[3] = True
    primes = [i for (i, s) in zip(range(3, lim12, 2), l) if s]
    for (i, p) in enumerate((3, 5, 7)):
        primes[i] = p
    res = False
    for x in (n, n - 2, n - 4):
        if x > primes[-1]:
            for p in primes:
                if not x % p:
                    break
            else:
                res = True
        else:
            res = x in primes
        if res:
            k = (n - x) // 2 + 1
            return (k, [x] + [2] * ((n - x) // 2))
    (l, cache) = ([], set())
    for b in primes:
        l.append(b)
        for c in l:
            a = n - b - c
            if a not in cache:
                for p in primes:
                    if not a % p:
                        cache.add(a)
                        break
                else:
                    return (3, [a, b, c])