"""
QUESTION:
The construction of subway in Bertown is almost finished! The President of Berland will visit this city soon to look at the new subway himself.

There are n stations in the subway. It was built according to the Bertown Transport Law:

  For each station i there exists exactly one train that goes from this station. Its destination station is p_{i}, possibly p_{i} = i;  For each station i there exists exactly one station j such that p_{j} = i. 

The President will consider the convenience of subway after visiting it. The convenience is the number of ordered pairs (x, y) such that person can start at station x and, after taking some subway trains (possibly zero), arrive at station y (1 ≤ x, y ≤ n).

The mayor of Bertown thinks that if the subway is not convenient enough, then the President might consider installing a new mayor (and, of course, the current mayor doesn't want it to happen). Before President visits the city mayor has enough time to rebuild some paths of subway, thus changing the values of p_{i} for not more than two subway stations. Of course, breaking the Bertown Transport Law is really bad, so the subway must be built according to the Law even after changes.

The mayor wants to do these changes in such a way that the convenience of the subway is maximized. Help him to calculate the maximum possible convenience he can get! 


-----Input-----

The first line contains one integer number n (1 ≤ n ≤ 100000) — the number of stations.

The second line contains n integer numbers p_1, p_2, ..., p_{n} (1 ≤ p_{i} ≤ n) — the current structure of the subway. All these numbers are distinct.


-----Output-----

Print one number — the maximum possible value of convenience.


-----Examples-----
Input
3
2 1 3

Output
9

Input
5
1 5 4 3 2

Output
17



-----Note-----

In the first example the mayor can change p_2 to 3 and p_3 to 1, so there will be 9 pairs: (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3).

In the second example the mayor can change p_2 to 4 and p_3 to 5.
"""

class Unionfind:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [1] * n

    def root(self, x):
        p = x
        while not self.par[p] < 0:
            p = self.par[p]
        while x != p:
            tmp = x
            x = self.par[x]
            self.par[tmp] = p
        return p

    def unite(self, x, y):
        (rx, ry) = (self.root(x), self.root(y))
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            (rx, ry) = (ry, rx)
        self.par[rx] += self.par[ry]
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def count(self, x):
        return -self.par[self.root(x)]

def calculate_max_convenience(n, p):
    uf = Unionfind(n)
    for i in range(n):
        uf.unite(i, p[i] - 1)
    
    rs = set((uf.root(i) for i in range(n)))
    l = []
    for r in rs:
        l.append(uf.count(r))
    
    l.sort(reverse=True)
    
    if len(l) == 1:
        return n * n
    
    max_convenience = (l[0] + l[1]) ** 2
    for i in range(2, len(l)):
        max_convenience += l[i] ** 2
    
    return max_convenience