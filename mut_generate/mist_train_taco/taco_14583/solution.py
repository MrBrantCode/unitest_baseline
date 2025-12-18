"""
QUESTION:
Little X has n distinct integers: p1, p2, ..., pn. He wants to divide all of them into two sets A and B. The following two conditions must be satisfied:

  * If number x belongs to set A, then number a - x must also belong to set A. 
  * If number x belongs to set B, then number b - x must also belong to set B. 



Help Little X divide the numbers into two sets or determine that it's impossible.

Input

The first line contains three space-separated integers n, a, b (1 ≤ n ≤ 105; 1 ≤ a, b ≤ 109). The next line contains n space-separated distinct integers p1, p2, ..., pn (1 ≤ pi ≤ 109).

Output

If there is a way to divide the numbers into two sets, then print "YES" in the first line. Then print n integers: b1, b2, ..., bn (bi equals either 0, or 1), describing the division. If bi equals to 0, then pi belongs to set A, otherwise it belongs to set B.

If it's impossible, print "NO" (without the quotes).

Examples

Input

4 5 9
2 3 4 5


Output

YES
0 0 1 1


Input

3 3 4
1 2 4


Output

NO

Note

It's OK if all the numbers are in the same set, and the other one is empty.
"""

class DisjointSet:
    def __init__(self, n):
        self._fa = list(range(n))

    def union(self, x, y):
        x = self.get_father(x)
        y = self.get_father(y)
        self._fa[x] = y
        return y

    def get_father(self, x):
        y = self._fa[x]
        if self._fa[y] == y:
            return y
        else:
            z = self._fa[y] = self.get_father(y)
            return z

def divide_numbers_into_sets(n, a, b, xs):
    h = {x: i for (i, x) in enumerate(xs)}
    if a == b:
        if all((a - x in h for x in xs)):
            return "YES", [0] * n
        return "NO"
    
    g1 = n
    g2 = n + 1
    ds = DisjointSet(n + 2)
    
    for (i, x) in enumerate(xs):
        for t in (a, b):
            if t - x in h:
                ds.union(i, h[t - x])
    
    for (i, x) in enumerate(xs):
        b1 = a - x in h
        b2 = b - x in h
        if b1 + b2 == 0:
            return "NO"
        if b1 + b2 == 1:
            if b1:
                ds.union(i, g1)
            else:
                ds.union(i, g2)
            if ds.get_father(g1) == ds.get_father(g2):
                return "NO"
    
    group = [None] * n
    for (i, x) in enumerate(xs):
        f = ds.get_father(i)
        if f < n:
            return "NO"
        group[i] = f - n
    
    return "YES", group