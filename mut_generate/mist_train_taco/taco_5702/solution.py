"""
QUESTION:
Parmida is a clever girl and she wants to participate in Olympiads this year. Of course she wants her partner to be clever too (although he's not)! Parmida has prepared the following test problem for Pashmak.

There is a sequence a that consists of n integers a_1, a_2, ..., a_{n}. Let's denote f(l, r, x) the number of indices k such that: l ≤ k ≤ r and a_{k} = x. His task is to calculate the number of pairs of indicies i, j (1 ≤ i < j ≤ n) such that f(1, i, a_{i}) > f(j, n, a_{j}).

Help Pashmak with the test.


-----Input-----

The first line of the input contains an integer n (1 ≤ n ≤ 10^6). The second line contains n space-separated integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9).


-----Output-----

Print a single integer — the answer to the problem.


-----Examples-----
Input
7
1 2 1 1 2 2 1

Output
8

Input
3
1 1 1

Output
1

Input
5
1 2 3 4 5

Output
0
"""

def count_clever_pairs(n, a):
    BIT = [0] * (10 ** 6)

    def update(idx):
        while idx < len(BIT):
            BIT[idx] += 1
            idx += idx & -idx

    def query(idx):
        s = 0
        while idx > 0:
            s += BIT[idx]
            idx -= idx & -idx
        return s

    ans = 0
    cnt = {}
    l = [0] * n
    r = [0] * n
    
    for i in range(n):
        cnt[a[i]] = cnt.get(a[i], 0) + 1
        l[i] = cnt[a[i]]
    
    cnt.clear()
    
    for i in range(n)[::-1]:
        cnt[a[i]] = cnt.get(a[i], 0) + 1
        r[i] = cnt[a[i]]
        if i < n - 1:
            ans += query(l[i] - 1)
        update(r[i])
    
    return ans