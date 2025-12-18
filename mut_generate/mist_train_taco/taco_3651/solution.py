"""
QUESTION:
John lives in HackerLand, a country with $N$ cities and $\mbox{M}$ bidirectional roads. Each of the roads has a distinct length, and each length is a power of two (i.e., $2$ raised to some exponent). It's possible for John to reach any city from any other city.

Given a map of HackerLand, can you help John determine the sum of the minimum distances between each pair of cities? Print your answer in binary representation. 

Input Format

The first line contains two space-seperated integers denoting $N$ (the number of cities) and $\mbox{M}$ (the number of roads), respectively. 

Each line $\boldsymbol{i}$ of the $\mbox{M}$ subsequent lines contains the respective values of $A_i$, $B_i$, and $C_i$ as three space-separated integers. These values define a bidirectional road between cities $A_i$ and $B_i$ having length $2^{C_i}$.

Constraints

$1\leq N\leq10^5$
$1\leq M\leq2\times10^5$
$1\leq A_i,B_i\leq N$, $A_i\neq B_i$
$0\leq C_i<M$
If $i\neq j$, then $C_i\neq C_j$.

Output Format

Find the sum of minimum distances of each pair of cities and print the answer in binary representation. 

Sample Input
5 6
1 3 5
4 5 0
2 1 3
3 2 1
4 3 4
4 2 2

Sample Output
1000100

Explanation

In the sample, the country looks like this:

Let $d(x,y)$ be the minimum distance between city $\boldsymbol{x}$ and city $y$. 

$d(1,2)=8$

$d(1,3)=10$

$d(1,4)=12$

$d(1,5)=13$

$d(2,3)=2$

$d(2,4)=4$

$d(2,5)=5$

$d(3,4)=6$

$d(3,5)=7$

$d(4,5)=1$

$Sum=8+10+12+13+2+4+5+6+7+1=(68)_{10}=(1000100)_{2}$
"""

def calculate_minimum_distances_sum(n, m, roads):
    p = list(range(n))

    def dsu_get(v):
        if p[v] != v:
            p[v] = dsu_get(p[v])
        return p[v]

    def dsu_merge(u, v):
        u = dsu_get(u)
        v = dsu_get(v)
        p[u] = v
        return u != v

    e = []
    for (a, b, c) in roads:
        e.append((c, a - 1, b - 1))
    e.sort()

    G = [[] for _ in range(n)]
    for (c, a, b) in e:
        if dsu_merge(a, b):
            G[a].append((b, c))
            G[b].append((a, c))

    f = [0] * m

    def dfs(v, par=-1):
        sz = 1
        for (u, c) in G[v]:
            if u == par:
                continue
            y = dfs(u, v)
            f[c] = y * (n - y)
            sz += y
        return sz

    dfs(0)
    ans = 0
    for x in f[::-1]:
        ans *= 2
        ans += x
    return bin(ans)[2:]