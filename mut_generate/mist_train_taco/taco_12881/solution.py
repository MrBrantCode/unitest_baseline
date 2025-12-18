"""
QUESTION:
Count the number of distinct sequences a_1, a_2, ..., a_{n} (1 ≤ a_{i}) consisting of positive integers such that gcd(a_1, a_2, ..., a_{n}) = x and $\sum_{i = 1}^{n} a_{i} = y$. As this number could be large, print the answer modulo 10^9 + 7.

gcd here means the greatest common divisor.


-----Input-----

The only line contains two positive integers x and y (1 ≤ x, y ≤ 10^9).


-----Output-----

Print the number of such sequences modulo 10^9 + 7.


-----Examples-----
Input
3 9

Output
3

Input
5 8

Output
0



-----Note-----

There are three suitable sequences in the first test: (3, 3, 3), (3, 6), (6, 3).

There are no suitable sequences in the second test.
"""

def count_distinct_sequences(x: int, y: int) -> int:
    mod = 1000000007

    def modpow(a, x):
        if x == 0:
            return 1
        if x == 1:
            return a
        b = modpow(a, x // 2)
        return b * b * a ** (x % 2) % mod

    if y % x != 0:
        return 0
    if x == y:
        return 1

    a = y // x
    divs = []
    i = 2
    while i * i < a:
        if a % i == 0:
            divs.append(i)
            divs.append(a // i)
        i += 1
    if int(a ** 0.5) ** 2 == a:
        divs.append(int(a ** 0.5))
    divs.append(a)
    divs.sort()

    res = modpow(2, a - 1)
    muls = [0 for _ in divs]
    muls[0] = 1
    for (xid, d) in enumerate(divs):
        prevs = 0
        for (id, d2) in enumerate(divs):
            if d2 < d and d % d2 == 0:
                prevs += muls[id]
        muls[xid] = 1 - prevs
        res += (prevs - 1) * modpow(2, a // d - 1)
        res = (res + 1000 * mod) % mod

    return res