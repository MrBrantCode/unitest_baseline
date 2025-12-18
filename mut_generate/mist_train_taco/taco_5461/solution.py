"""
QUESTION:
This problem is a complicated version of D1, but it has significant differences, so read the whole statement.

Polycarp has an array of $n$ ($n$ is even) integers $a_1, a_2, \dots, a_n$. Polycarp conceived of a positive integer $k$. After that, Polycarp began performing the following operations on the array: take an index $i$ ($1 \le i \le n$) and reduce the number $a_i$ by $k$.

After Polycarp performed some (possibly zero) number of such operations, it turned out that at least half of the numbers in the array became the same. Find the maximum $k$ at which such a situation is possible, or print $-1$ if such a number can be arbitrarily large.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10$) — the number of test cases. Then $t$ test cases follow.

Each test case consists of two lines. The first line contains an even integer $n$ ($4 \le n \le 40$) ($n$ is even). The second line contains $n$ integers $a_1, a_2, \dots a_n$ ($-10^6 \le a_i \le 10^6$).

It is guaranteed that the sum of all $n$ specified in the given test cases does not exceed $100$.


-----Output-----

For each test case output on a separate line an integer $k$ ($k \ge 1$) — the maximum possible number that Polycarp used in operations on the array, or $-1$, if such a number can be arbitrarily large.


-----Examples-----

Input
4
6
48 13 22 -15 16 35
8
-1 0 1 -1 0 1 -1 0
4
100 -1000 -1000 -1000
4
1 1 1 1
Output
13
2
-1
-1


-----Note-----

None
"""

import math

memo = {}

def divisors(n):
    if n in memo:
        return memo[n]
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, int(n / i)])
    divs.extend([n])
    memo[n] = list(set(divs))
    return memo[n]

def find_max_k(test_cases):
    results = []
    for (n, nums) in test_cases:
        mxK = 0
        for j in nums:
            diff = [x - j for x in nums]
            k = max(diff)
            cnt = diff.count(0)
            if cnt >= n / 2:
                mxK = -1
                break
            cnt_div = {}
            for i in diff:
                if i > 0:
                    divs = divisors(i)
                    for d in divs:
                        cnt_div[d] = cnt_div.get(d, 0) + 1
            cnt_div = sorted(cnt_div.items(), reverse=True)
            for (u, v) in cnt_div:
                if v + cnt >= n / 2:
                    mxK = max(mxK, u)
        results.append(mxK if mxK > 0 else -1)
    return results