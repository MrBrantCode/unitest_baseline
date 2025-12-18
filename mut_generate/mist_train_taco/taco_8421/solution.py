"""
QUESTION:
You are given two positive integer numbers x and y. An array F is called an y-factorization of x iff the following conditions are met:  There are y elements in F, and all of them are integer numbers;  $\prod_{i = 1}^{y} F_{i} = x$. 

You have to count the number of pairwise distinct arrays that are y-factorizations of x. Two arrays A and B are considered different iff there exists at least one index i (1 ≤ i ≤ y) such that A_{i} ≠ B_{i}. Since the answer can be very large, print it modulo 10^9 + 7.


-----Input-----

The first line contains one integer q (1 ≤ q ≤ 10^5) — the number of testcases to solve.

Then q lines follow, each containing two integers x_{i} and y_{i} (1 ≤ x_{i}, y_{i} ≤ 10^6). Each of these lines represents a testcase.


-----Output-----

Print q integers. i-th integer has to be equal to the number of y_{i}-factorizations of x_{i} modulo 10^9 + 7.


-----Example-----
Input
2
6 3
4 2

Output
36
6



-----Note-----

In the second testcase of the example there are six y-factorizations:  { - 4,  - 1};  { - 2,  - 2};  { - 1,  - 4};  {1, 4};  {2, 2};  {4, 1}.
"""

def count_y_factorizations(x: int, y: int, md: int = 10**9 + 7) -> int:
    def cnk(n: int, k: int) -> int:
        if k > n // 2:
            k = n - k
        ans = 1
        for i in range(n - k + 1, n + 1):
            ans *= i
        for i in range(2, k + 1):
            ans //= i
        ans = ans % md
        return ans

    def factor(n: int) -> list[int]:
        pws = []
        dv = 2
        lp = 0
        while n % dv == 0:
            lp += 1
            n //= dv
        if lp:
            pws.append(lp)
        dv = 3
        while n > 1 and dv * dv <= n:
            lp = 0
            while n % dv == 0:
                lp += 1
                n //= dv
            if lp:
                pws.append(lp)
            dv += 2
        if n > 1:
            pws.append(1)
        return pws

    ans = pow(2, y - 1, md)
    for f in factor(x):
        cm = cnk(f + y - 1, y - 1)
        ans = ans * cm % md
    return ans