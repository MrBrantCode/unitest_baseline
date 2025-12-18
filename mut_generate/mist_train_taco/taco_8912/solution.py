"""
QUESTION:
Chef has entered the politics of Byteland. He is a minister in the coal department of the government. Recently, he has been assigned a project on constructing special bidirectional roads for transferring coals in such a way that the whole country is connected by a road network.

Different companies submitted their proposal of roads that they could build along with their estimated cost of the road. Chef has to select a subset of these proposed roads so that all cities of the country are connected.

Chef, corrupt as he is, managed to submit bids by his own company for certain roads. If some of his proposed roads are selected, he'd use low grade material. We can safely assume that the cost of building these roads is nothing to him. He would still receive the price he has quoted in the bid and hence, would make as much profit. He wants to choose some subset of proposed roads so that his own profit is maximised.

Byteland consists of N cities. There are M1 proposals to build roads by companies other than Chef's. Chef's company has proposed to build M2 roads. Chef wants to choose a subset of these roads in such a way that for each pair of cities, there is exactly one path of roads connecting them. The profit Chef will gain is equal to the sum of costs of the roads chosen from among those made by Chef's company.

Help Chef choose the roads in such a way that his profit is maximized. If there are multiple ways to achieve that, choose the way where the sum of costs of all chosen roads is minimized.

------ Input ------ 

The first line of the input contains a number T, the number of test cases. This is followed by the input for each test case one by one. The first line of each test case contains three space-separated integers N, M1, and M2. Then M1 lines follow, each containing a description of a road proposed by other companies. Each of these lines contains three space-separated integers u, v, and c, where u and v denote the end points of the road and c denotes the associated cost. Then M2 lines follow, each containing a description of a road proposed by Chef's company in the same format.

------ Output ------ 

Output a single line for each test case. If it is impossible to choose a subset of the roads in such a way that for each pair of cities, there is exactly one path of roads connecting them, output a single line containing "Impossible" (quotes for clarity and starts with an uppercase 'I') for that test case. Otherwise, output a single line containing two space-separated integers: the maximum profit Chef can gain and the minimum total cost of the chosen roads that yields the maximum profit.

------ Constraints ------ 

1 ≤ T ≤ 5

2 ≤ N ≤ 5,000

1 ≤ M1 ≤ 20,000

1 ≤ M2 ≤ 20,000

For each proposed road, the end points will be two different cities.

There may be several proposed roads between the same pair of cities.

For each proposed road, 0 ≤ c ≤ 1,000,000,000

Each input file will not be larger than 4 MB (4,000,000,000 bytes) in size.

----- Sample Input 1 ------ 
2
3 2 1
0 1 5
1 2 4
0 1 10
3 1 1
0 1 1
0 1 3
----- Sample Output 1 ------ 
10 14
Impossible
"""

from collections import defaultdict

class dsu:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [0] * (n + 1)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u != v:
            self.parent[v] = u

    def check(self, n):
        cnt = 0
        for i in range(n):
            if self.parent[i] == i:
                cnt += 1
        return cnt > 1

def maximize_chef_profit(T, test_cases):
    results = []
    for case in test_cases:
        N, M1, M2, company_roads, chef_roads = case
        company_roads.sort()
        chef_roads.sort(reverse=True)
        d = dsu(N)
        chef_cost, company_cost = 0, 0

        for (w, u, v) in chef_roads:
            if d.find(u) != d.find(v):
                d.union(u, v)
                chef_cost += w

        for (w, u, v) in company_roads:
            if d.find(u) != d.find(v):
                d.union(u, v)
                company_cost += w

        if d.check(N):
            results.append(("Impossible",))
        else:
            results.append((chef_cost, company_cost + chef_cost))

    return results