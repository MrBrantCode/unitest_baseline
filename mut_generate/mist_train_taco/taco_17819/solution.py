"""
QUESTION:
Let's call a non-empty sequence of positive integers a_1, a_2... a_{k} coprime if the greatest common divisor of all elements of this sequence is equal to 1.

Given an array a consisting of n positive integers, find the number of its coprime subsequences. Since the answer may be very large, print it modulo 10^9 + 7.

Note that two subsequences are considered different if chosen indices are different. For example, in the array [1, 1] there are 3 different subsequences: [1], [1] and [1, 1].


-----Input-----

The first line contains one integer number n (1 ≤ n ≤ 100000).

The second line contains n integer numbers a_1, a_2... a_{n} (1 ≤ a_{i} ≤ 100000).


-----Output-----

Print the number of coprime subsequences of a modulo 10^9 + 7.


-----Examples-----
Input
3
1 2 3

Output
5

Input
4
1 1 1 1

Output
15

Input
7
1 3 5 15 3 105 35

Output
100



-----Note-----

In the first example coprime subsequences are:   1  1, 2  1, 3  1, 2, 3  2, 3 

In the second example all subsequences are coprime.
"""

import sys
import math

MOD = 10 ** 9 + 7

def count_coprime_subsequences(n, a):
    def getMul(x):
        a = 1
        for xi in x:
            a *= xi
        return a

    d = {}
    for ai in a:
        if ai in d:
            d[ai] += 1
        else:
            d[ai] = 1

    f = [[] for i in range(max(a) + 10)]
    for i in range(1, len(f)):
        for j in range(i, len(f), i):
            f[j].append(i)

    seq = [0 for i in range(max(a) + 10)]
    for ai in d:
        for fi in f[ai]:
            seq[fi] += d[ai]

    for i in range(len(seq)):
        seq[i] = (pow(2, seq[i], MOD) - 1 + MOD) % MOD

    pf = [[] for i in range(max(a) + 10)]
    pf[0] = None
    pf[1].append(1)
    for i in range(2, len(f)):
        if len(pf[i]) == 0:
            for j in range(i, len(pf), i):
                pf[j].append(i)

    for i in range(1, len(pf)):
        mul = getMul(pf[i])
        if mul == i:
            if len(pf[i]) & 1 == 1:
                pf[i] = -1
            else:
                pf[i] = 1
        else:
            pf[i] = 0

    pf[1] = 1
    ans = 0
    for i in range(1, len(seq)):
        ans += seq[i] * pf[i]
        ans = (ans + MOD) % MOD

    return ans