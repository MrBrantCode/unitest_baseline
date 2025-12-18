"""
QUESTION:
You are given a rectangular parallelepiped with sides of positive integer lengths $A$, $B$ and $C$. 

Find the number of different groups of three integers ($a$, $b$, $c$) such that $1\leq a\leq b\leq c$ and parallelepiped $A\times B\times C$ can be paved with parallelepipeds $a\times b\times c$. Note, that all small parallelepipeds have to be rotated in the same direction.

For example, parallelepiped $1\times 5\times 6$ can be divided into parallelepipeds $1\times 3\times 5$, but can not be divided into parallelepipeds $1\times 2\times 3$.


-----Input-----

The first line contains a single integer $t$ ($1 \leq t \leq 10^5$) — the number of test cases.

Each of the next $t$ lines contains three integers $A$, $B$ and $C$ ($1 \leq A, B, C \leq 10^5$) — the sizes of the parallelepiped.


-----Output-----

For each test case, print the number of different groups of three points that satisfy all given conditions.


-----Example-----
Input
4
1 1 1
1 6 1
2 2 2
100 100 100

Output
1
4
4
165



-----Note-----

In the first test case, rectangular parallelepiped $(1, 1, 1)$ can be only divided into rectangular parallelepiped with sizes $(1, 1, 1)$.

In the second test case, rectangular parallelepiped $(1, 6, 1)$ can be divided into rectangular parallelepipeds with sizes $(1, 1, 1)$, $(1, 1, 2)$, $(1, 1, 3)$ and $(1, 1, 6)$.

In the third test case, rectangular parallelepiped $(2, 2, 2)$ can be divided into rectangular parallelepipeds with sizes $(1, 1, 1)$, $(1, 1, 2)$, $(1, 2, 2)$ and $(2, 2, 2)$.
"""

from math import gcd

def count_paving_groups(A, B, C):
    d = [3.0, 1.0, 2.0, 2.0, 2.0, 1.0] * 16667
    for i in range(4, 100001):
        for j in range(i, 100001, i):
            d[j] += 1.0
    
    k = gcd(B, C)
    ab = d[gcd(A, B)]
    ac = d[gcd(A, C)]
    bc = d[k]
    abc = d[gcd(A, k)]
    
    asz = d[A] - ab - ac + abc
    bsz = d[B] - bc - ab + abc
    csz = d[C] - ac - bc + abc
    absz = ab - abc
    bcsz = bc - abc
    acsz = ac - abc
    
    result = int(asz * bsz * csz + absz * (asz + bsz) * csz + bcsz * (bsz + csz) * asz + acsz * (asz + csz) * bsz + abc * (asz * bsz + asz * csz + bsz * csz) + abc * (absz + bcsz + acsz) * (asz + bsz + csz) + (asz + bsz + csz + absz + bcsz + acsz) * (abc * (abc + 1) * 0.5) + absz * bcsz * acsz + (absz * (absz + 1.0) * d[C] + bcsz * (bcsz + 1.0) * d[A] + acsz * (acsz + 1.0) * d[B]) * 0.5 + (asz + bsz + csz + abc) * (absz * acsz + absz * bcsz + bcsz * acsz) + (abc + abc * (abc - 1.0) + abc * (abc - 1.0) * (abc - 2.0) / 6.0))
    
    return result