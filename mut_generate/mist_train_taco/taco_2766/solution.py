"""
QUESTION:
Eric is the teacher of graph theory class. Today, Eric teaches independent set and edge-induced subgraph.

Given a graph $G=(V,E)$, an independent set is a subset of vertices $V' \subset V$ such that for every pair $u,v \in V'$, $(u,v) \not \in E$ (i.e. no edge in $E$ connects two vertices from $V'$).

An edge-induced subgraph consists of a subset of edges $E' \subset E$ and all the vertices in the original graph that are incident on at least one edge in the subgraph.

Given $E' \subset E$, denote $G[E']$ the edge-induced subgraph such that $E'$ is the edge set of the subgraph. Here is an illustration of those definitions: [Image] 

In order to help his students get familiar with those definitions, he leaves the following problem as an exercise:

Given a tree $G=(V,E)$, calculate the sum of $w(H)$ over all except null edge-induced subgraph $H$ of $G$, where $w(H)$ is the number of independent sets in $H$. Formally, calculate $\sum \limits_{\emptyset \not= E' \subset E} w(G[E'])$.

Show Eric that you are smarter than his students by providing the correct answer as quickly as possible. Note that the answer might be large, you should output the answer modulo $998,244,353$.


-----Input-----

The first line contains a single integer $n$ ($2 \le n \le 3 \cdot 10^5$), representing the number of vertices of the graph $G$.

Each of the following $n-1$ lines contains two integers $u$ and $v$ ($1 \le u,v \le n$, $u \not= v$), describing edges of the given tree.

It is guaranteed that the given edges form a tree.


-----Output-----

Output one integer, representing the desired value modulo $998,244,353$.


-----Examples-----
Input
2
2 1

Output
3

Input
3
1 2
3 2

Output
11



-----Note-----

For the second example, all independent sets are listed below. $\vdots : \vdots : \vdots$
"""

def calculate_independent_set_sum(n, edges):
    mod = 998244353
    E = [[] for _ in range(n + 1)]
    
    for u, v in edges:
        E[u].append(v)
        E[v].append(u)
    
    ROOT = 1
    QUE = [ROOT]
    Parent = [-1] * (n + 1)
    Parent[ROOT] = n + 1
    TOP_SORT = []
    
    while QUE:
        x = QUE.pop()
        TOP_SORT.append(x)
        for to in E[x]:
            if Parent[to] == -1:
                Parent[to] = x
                QUE.append(to)
    
    DP0 = [1] * (n + 1)
    DP1 = [1] * (n + 1)
    DP2 = [1] * (n + 1)
    DP3 = [1] * (n + 1)
    
    for x in TOP_SORT[::-1]:
        if x != 1 and len(E[x]) == 1:
            DP0[x] = 1
            DP1[x] = 1
            DP2[x] = 0
            DP3[x] = 1
            continue
        
        ANS0 = 1
        ANS2 = 1
        ANS3 = 1
        
        for to in E[x]:
            if to == Parent[x]:
                continue
            ANS0 = ANS0 * (DP0[to] + DP1[to] + DP2[to] + DP3[to]) % mod
            ANS2 = ANS2 * (DP0[to] + DP2[to]) % mod
            ANS3 = ANS3 * (DP0[to] + DP1[to] + DP2[to]) % mod
        
        DP0[x] = ANS0
        DP1[x] = ANS0
        DP2[x] = ANS3 - ANS2
        DP3[x] = ANS3
    
    return (DP0[1] + DP2[1] - 1) % mod