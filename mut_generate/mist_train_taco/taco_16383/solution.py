"""
QUESTION:
Determine whether a text T includes a pattern P. Your program should answer for given queries consisting of P_i.

Constraints

* 1 ≤ length of T ≤ 1000000
* 1 ≤ length of P_i ≤ 1000
* 1 ≤ Q ≤ 10000
* The input consists of alphabetical characters and digits

Input

In the first line, a text T is given. In the second line, an integer Q denoting the number of queries is given. In the following Q lines, the patterns P_i are given respectively.

Output

For each question, print 1 if the text includes P_i, or print 0 otherwise.

Example

Input

aabaaa
4
aa
ba
bb
xyz


Output

1
1
0
0
"""

def pattern_in_text(T: str, patterns: list[str]) -> list[int]:
    base = 127
    mask = (1 << 32) - 1

    def calc_hash(f, pl, tl):
        dl = tl - pl
        tmp = set()
        t = 1
        for _ in range(pl):
            t = t * base & mask
        e = 0
        for i in range(pl):
            e = e * base + f[i] & mask
        for i in range(dl):
            tmp.add(e)
            e = e * base - t * f[i] + f[i + pl] & mask
        tmp.add(e)
        return tmp

    t = tuple((ord(c) for c in T))
    tl = len(t)
    h = dict()
    c = dict()
    results = []

    for p in patterns:
        if p in c:
            results.append(c[p])
            continue
        p = tuple((ord(c) for c in p))
        pl = len(p)
        if pl > tl:
            results.append(0)
            continue
        bs = min(19, pl)
        keys = calc_hash(p, bs, pl)
        if bs not in h:
            h[bs] = calc_hash(t, bs, tl)
        results.append(1 if keys.issubset(h[bs]) else 0)
    
    return results