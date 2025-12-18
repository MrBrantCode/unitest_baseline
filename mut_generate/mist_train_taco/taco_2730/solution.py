"""
QUESTION:
Monocarp plays a computer game (yet again!). This game has a unique trading mechanics.

To trade with a character, Monocarp has to choose one of the items he possesses and trade it for some item the other character possesses. Each item has an integer price. If Monocarp's chosen item has price $x$, then he can trade it for any item (exactly one item) with price not greater than $x+k$.

Monocarp initially has $n$ items, the price of the $i$-th item he has is $a_i$. The character Monocarp is trading with has $m$ items, the price of the $i$-th item they have is $b_i$. Monocarp can trade with this character as many times as he wants (possibly even zero times), each time exchanging one of his items with one of the other character's items according to the aforementioned constraints. Note that if Monocarp gets some item during an exchange, he can trade it for another item (since now the item belongs to him), and vice versa: if Monocarp trades one of his items for another item, he can get his item back by trading something for it.

You have to answer $q$ queries. Each query consists of one integer, which is the value of $k$, and asks you to calculate the maximum possible total cost of items Monocarp can have after some sequence of trades, assuming that he can trade an item of cost $x$ for an item of cost not greater than $x+k$ during each trade. Note that the queries are independent: the trades do not actually occur, Monocarp only wants to calculate the maximum total cost he can get.


-----Input-----

The first line contains three integers $n$, $m$ and $q$ ($1 \le n, m, q \le 2 \cdot 10^5$).

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^9$) — the prices of the items Monocarp has.

The third line contains $m$ integers $b_1, b_2, \dots, b_m$ ($1 \le b_i \le 10^9$) — the prices of the items the other character has.

The fourth line contains $q$ integers, where the $i$-th integer is the value of $k$ for the $i$-th query ($0 \le k \le 10^9$).


-----Output-----

For each query, print one integer — the maximum possible total cost of items Monocarp can have after some sequence of trades, given the value of $k$ from the query.


-----Examples-----

Input
3 4 5
10 30 15
12 31 14 18
0 1 2 3 4
Output
55
56
60
64
64


-----Note-----

None
"""

import bisect
from itertools import accumulate

def calculate_max_total_cost(n, m, q, a, b, queries):
    nums = a + b
    nums.sort()
    a.sort()
    sums = [0] + list(accumulate(nums))
    nm = n + m
    f = list(range(nm))
    cnt = [0] * nm
    mx = sum(a)

    def find(i):
        if i != f[i]:
            f[i] = find(f[i])
        return f[i]

    def union(i, j):
        fi, fj = find(i), find(j)
        if fi != fj:
            if fi < fj:
                fi, fj = fj, fi
            f[fj] = fi
            l1, l2 = cnt[fi], cnt[fj]
            l3 = l1 + l2
            cnt[fi] = l3
            nonlocal mx
            mx += sums[fi + 1 - l1] - sums[fi + 1 - l3] - (sums[fj + 1] - sums[fj + 1 - l2])

    i, j = 0, 0
    while i < n:
        while a[i] != nums[j]:
            j += 1
        cnt[j] = 1
        i += 1
        j += 1

    mg = []
    ans = [0] * q
    for i in range(nm - 1):
        mg.append((nums[i + 1] - nums[i], i, i + 1))
    mg.sort(key=lambda it: it[0], reverse=True)

    for k, ai in sorted(zip(queries, range(q))):
        while mg and mg[-1][0] <= k:
            _, i, j = mg.pop()
            union(i, j)
        ans[ai] = mx

    return ans