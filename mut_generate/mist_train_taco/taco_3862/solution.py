"""
QUESTION:
You are given $a$ uppercase Latin letters 'A' and $b$ letters 'B'.

The period of the string is the smallest such positive integer $k$ that $s_i = s_{i~mod~k}$ ($0$-indexed) for each $i$. Note that this implies that $k$ won't always divide $a+b = |s|$.

For example, the period of string "ABAABAA" is $3$, the period of "AAAA" is $1$, and the period of "AABBB" is $5$.

Find the number of different periods over all possible strings with $a$ letters 'A' and $b$ letters 'B'.


-----Input-----

The first line contains two integers $a$ and $b$ ($1 \le a, b \le 10^9$) — the number of letters 'A' and 'B', respectively.


-----Output-----

Print the number of different periods over all possible strings with $a$ letters 'A' and $b$ letters 'B'.


-----Examples-----
Input
2 4

Output
4

Input
5 3

Output
5



-----Note-----

All the possible periods for the first example:   $3$ "BBABBA"  $4$ "BBAABB"  $5$ "BBBAAB"  $6$ "AABBBB" 

All the possible periods for the second example:   $3$ "BAABAABA"  $5$ "BAABABAA"  $6$ "BABAAABA"  $7$ "BAABAAAB"  $8$ "AAAAABBB" 

Note that these are not the only possible strings for the given periods.
"""

import math

def count_different_periods(a: int, b: int) -> int:
    n = a + b
    ans = 0
    l = 1
    while l <= n:
        g = n // l
        if a < g or b < g:
            l = n // g + 1
            continue
        r = n // g
        a_low = (a + g) // (g + 1)
        a_high = a // g
        b_low = (b + g) // (g + 1)
        b_high = b // g
        if a_low <= a_high and b_low <= b_high:
            ans += max(0, min(r, a_high + b_high) - max(l, a_low + b_low) + 1)
        l = r + 1
    return ans