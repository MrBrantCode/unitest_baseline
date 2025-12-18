"""
QUESTION:
This problem is a simplified version of D2, but it has significant differences, so read the whole statement.

Polycarp has an array of $n$ ($n$ is even) integers $a_1, a_2, \dots, a_n$. Polycarp conceived of a positive integer $k$. After that, Polycarp began performing the following operations on the array: take an index $i$ ($1 \le i \le n$) and reduce the number $a_i$ by $k$.

After Polycarp performed some (possibly zero) number of such operations, it turned out that all numbers in the array became the same. Find the maximum $k$ at which such a situation is possible, or print $-1$ if such a number can be arbitrarily large.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10$) — the number of test cases. Then $t$ test cases follow.

Each test case consists of two lines. The first line contains an even integer $n$ ($4 \le n \le 40$) ($n$ is even). The second line contains $n$ integers $a_1, a_2, \dots a_n$ ($-10^6 \le a_i \le 10^6$).

It is guaranteed that the sum of all $n$ specified in the given test cases does not exceed $100$.


-----Output-----

For each test case output on a separate line an integer $k$ ($k \ge 1$) — the maximum possible number that Polycarp used in operations on the array, or $-1$, if such a number can be arbitrarily large.


-----Examples-----

Input
3
6
1 5 3 1 1 5
8
-1 0 1 -1 0 1 -1 0
4
100 -1000 -1000 -1000
Output
2
1
1100


-----Note-----

None
"""

from math import gcd
from functools import reduce

def find_max_k(test_cases):
    results = []
    
    for n, a in test_cases:
        if len(set(a)) == 1:
            results.append(-1)
            continue
        
        b = min(a)
        k = reduce(gcd, (a_i - b for a_i in a))
        results.append(k)
    
    return results