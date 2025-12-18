"""
QUESTION:
There are N towns on a plane. The i-th town is located at the coordinates (x_i,y_i). There may be more than one town at the same coordinates.

You can build a road between two towns at coordinates (a,b) and (c,d) for a cost of min(|a-c|,|b-d|) yen (the currency of Japan). It is not possible to build other types of roads.

Your objective is to build roads so that it will be possible to travel between every pair of towns by traversing roads. At least how much money is necessary to achieve this?

Constraints

* 2 ≤ N ≤ 10^5
* 0 ≤ x_i,y_i ≤ 10^9
* All input values are integers.

Input

Input is given from Standard Input in the following format:


N
x_1 y_1
x_2 y_2
:
x_N y_N


Output

Print the minimum necessary amount of money in order to build roads so that it will be possible to travel between every pair of towns by traversing roads.

Examples

Input

3
1 5
3 9
7 8


Output

3


Input

6
8 3
4 9
12 19
18 1
13 5
7 6


Output

8
"""

def minimum_road_cost(towns):
    class UnionFind:
        def __init__(self, size):
            self.table = [-1 for _ in range(size)]

        def find(self, x):
            if self.table[x] < 0:
                return x
            else:
                self.table[x] = self.find(self.table[x])
                return self.table[x]

        def union(self, x, y):
            s1 = self.find(x)
            s2 = self.find(y)
            if s1 != s2:
                if self.table[s1] <= self.table[s2]:
                    self.table[s1] += self.table[s2]
                    self.table[s2] = s1
                else:
                    self.table[s2] += self.table[s1]
                    self.table[s1] = s2
                return True
            return False

    N = len(towns)
    a = [(towns[i][0], i) for i in range(N)]
    b = [(towns[i][1], i) for i in range(N)]
    a.sort()
    b.sort()
    
    t = []
    for i in range(1, N):
        t.append((a[i][0] - a[i - 1][0], a[i][1], a[i - 1][1]))
        t.append((b[i][0] - b[i - 1][0], b[i][1], b[i - 1][1]))
    t.sort()
    
    r = 0
    uf = UnionFind(N)
    for (c, d, e) in t:
        if uf.union(d, e):
            r += c
    
    return r