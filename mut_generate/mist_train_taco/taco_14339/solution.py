"""
QUESTION:
It is a simplified version of problem F2. The difference between them is the constraints (F1: $k \le 2$, F2: $k \le 10$).

You are given an integer $n$. Find the minimum integer $x$ such that $x \ge n$ and the number $x$ is $k$-beautiful.

A number is called $k$-beautiful if its decimal representation having no leading zeroes contains no more than $k$ different digits. E.g. if $k = 2$, the numbers $3434443$, $55550$, $777$ and $21$ are $k$-beautiful whereas the numbers $120$, $445435$ and $998244353$ are not.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10^4$) — the number of test cases. Then $t$ test cases follow.

Each test case consists of one line containing two integers $n$ and $k$ ($1 \le n \le 10^9$, $1 \le k \le 2$).


-----Output-----

For each test case output on a separate line $x$ — the minimum $k$-beautiful integer such that $x \ge n$.


-----Examples-----

Input
4
1 1
221 2
177890 2
998244353 1
Output
1
221
181111
999999999


-----Note-----

None
"""

from itertools import combinations
from bisect import bisect_left

# Precompute all possible k-beautiful numbers for k=1 and k=2
digits = [i for i in range(10)]

def get_all(length, digits, so_far=0):
    if length == 0:
        return [so_far]
    ret = []
    for d in digits:
        if so_far == 0 and d == 0:
            continue
        ret += get_all(length - 1, digits, so_far * 10 + d)
    return ret

all = []
all_1 = []
for length in range(1, 11):
    all_1 += [int(f'{x}' * length) for x in range(1, 10)]
    for p in combinations(digits, 2):
        p = list(p)
        all += get_all(length, p)

all_1.sort()
all += all_1
all.sort()

def find_min_k_beautiful_number(n, k):
    if k == 1:
        return all_1[bisect_left(all_1, n)]
    elif k == 2:
        return all[bisect_left(all, n)]
    else:
        raise ValueError("k must be 1 or 2")