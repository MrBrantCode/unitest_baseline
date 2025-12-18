"""
QUESTION:
Paladin Manao caught the trail of the ancient Book of Evil in a swampy area. This area contains n settlements numbered from 1 to n. Moving through the swamp is very difficult, so people tramped exactly n - 1 paths. Each of these paths connects some pair of settlements and is bidirectional. Moreover, it is possible to reach any settlement from any other one by traversing one or several paths.

The distance between two settlements is the minimum number of paths that have to be crossed to get from one settlement to the other one. Manao knows that the Book of Evil has got a damage range d. This means that if the Book of Evil is located in some settlement, its damage (for example, emergence of ghosts and werewolves) affects other settlements at distance d or less from the settlement where the Book resides.

Manao has heard of m settlements affected by the Book of Evil. Their numbers are p_1, p_2, ..., p_{m}. Note that the Book may be affecting other settlements as well, but this has not been detected yet. Manao wants to determine which settlements may contain the Book. Help him with this difficult task.


-----Input-----

The first line contains three space-separated integers n, m and d (1 ≤ m ≤ n ≤ 100000; 0 ≤ d ≤ n - 1). The second line contains m distinct space-separated integers p_1, p_2, ..., p_{m} (1 ≤ p_{i} ≤ n). Then n - 1 lines follow, each line describes a path made in the area. A path is described by a pair of space-separated integers a_{i} and b_{i} representing the ends of this path.


-----Output-----

Print a single number — the number of settlements that may contain the Book of Evil. It is possible that Manao received some controversial information and there is no settlement that may contain the Book. In such case, print 0.


-----Examples-----
Input
6 2 3
1 2
1 5
2 3
3 4
4 5
5 6

Output
3



-----Note-----

Sample 1. The damage range of the Book of Evil equals 3 and its effects have been noticed in settlements 1 and 2. Thus, it can be in settlements 3, 4 or 5.

 [Image]
"""

import collections

class Graph:
    def __init__(self, n, directed=False):
        self.node_cnt = n
        self.__directed = directed
        self.__adjList = [[] for _ in range(n)]

    def addEdge(self, u, v):
        self.__adjList[u].append(v)
        if not self.__directed:
            self.__adjList[v].append(u)

    def getDistances(self, start, end=None):
        assert 0 <= start < self.node_cnt
        dist = [-1] * self.node_cnt
        q = collections.deque()
        dist[start] = 0
        q.append(start)
        while q:
            z = q.popleft()
            if end == z:
                break
            for t in self.__adjList[z]:
                if dist[t] == -1:
                    dist[t] = dist[z] + 1
                    q.append(t)
                    if t == end:
                        break
        return dist

def getAffectedDiameter(graph, affected):
    affection = [False] * graph.node_cnt
    for x in affected:
        affection[x] = True
    dist0 = graph.getDistances(affected[0])
    affect_1 = max(range(graph.node_cnt), key=lambda i: dist0[i] if affection[i] else -1)
    dist1 = graph.getDistances(affect_1)
    affect_2 = max(range(graph.node_cnt), key=lambda i: dist1[i] if affection[i] else -1)
    return affect_1, affect_2

def find_possible_book_locations(n, m, d, affected, paths):
    g = Graph(n)
    for a, b in paths:
        g.addEdge(a, b)
    p1, p2 = getAffectedDiameter(g, affected)
    d1, d2 = g.getDistances(p1), g.getDistances(p2)
    cnt = sum(1 for i in range(n) if d1[i] <= d and d2[i] <= d)
    return cnt