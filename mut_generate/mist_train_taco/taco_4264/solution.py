"""
QUESTION:
You have a string of decimal digits s. Let's define b_{ij} = s_{i}·s_{j}. Find in matrix b the number of such rectangles that the sum b_{ij} for all cells (i, j) that are the elements of the rectangle equals a in each rectangle.

A rectangle in a matrix is a group of four integers (x, y, z, t) (x ≤ y, z ≤ t). The elements of the rectangle are all cells (i, j) such that x ≤ i ≤ y, z ≤ j ≤ t.


-----Input-----

The first line contains integer a (0 ≤ a ≤ 10^9), the second line contains a string of decimal integers s (1 ≤ |s| ≤ 4000).


-----Output-----

Print a single integer — the answer to a problem.

Please, do not write the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.


-----Examples-----
Input
10
12345

Output
6

Input
16
439873893693495623498263984765

Output
40
"""

def count_rectangles_with_sum(a: int, s: str) -> int:
    def divisors(x):
        def f(y, q):
            t = -len(r)
            while not y % q:
                y //= q
                for i in range(t, 0):
                    r.append(r[t] * q)
            return y
        (r, p) = ([1], 7)
        x = f(f(f(x, 2), 3), 5)
        while x >= p * p:
            for s in (4, 2, 4, 2, 4, 6, 2, 6):
                if not x % p:
                    x = f(x, p)
                p += s
        if x > 1:
            f(x, x)
        return r

    if not a:
        z = sum((x * (x + 1) for x in map(len, s.translate(str.maketrans('123456789', '         ')).split()))) // 2
        x = len(s)
        return (x * (x + 1) - z) * z

    (sums, x, cnt) = ({}, 0, 1)
    for u in map(int, s):
        if u:
            sums[x] = cnt
            x += u
            cnt = 1
        else:
            cnt += 1

    if x * x < a:
        return 0

    (sums[x], u) = (cnt, a // x)
    l = [v for v in divisors(a) if v <= x]
    z = a // max(l)
    d = {x: 0 for x in l if z <= x}
    for x in d:
        for (k, v) in list(sums.items()):
            u = sums.get(k + x, 0)
            if u:
                d[x] += v * u

    return sum((u * d[a // x] for (x, u) in list(d.items())))