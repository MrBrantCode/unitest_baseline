"""
QUESTION:
Someone give a strange birthday present to Ivan. It is hedgehog — connected undirected graph in which one vertex has degree at least 3 (we will call it center) and all other vertices has degree 1. Ivan thought that hedgehog is too boring and decided to make himself k-multihedgehog.

Let us define k-multihedgehog as follows:

  * 1-multihedgehog is hedgehog: it has one vertex of degree at least 3 and some vertices of degree 1.
  * For all k ≥ 2, k-multihedgehog is (k-1)-multihedgehog in which the following changes has been made for each vertex v with degree 1: let u be its only neighbor; remove vertex v, create a new hedgehog with center at vertex w and connect vertices u and w with an edge. New hedgehogs can differ from each other and the initial gift. 



Thereby k-multihedgehog is a tree. Ivan made k-multihedgehog but he is not sure that he did not make any mistakes. That is why he asked you to check if his tree is indeed k-multihedgehog.

Input

First line of input contains 2 integers n, k (1 ≤ n ≤ 10^{5}, 1 ≤ k ≤ 10^{9}) — number of vertices and hedgehog parameter.

Next n-1 lines contains two integers u v (1 ≤ u,    v ≤ n;    u ≠ v) — indices of vertices connected by edge.

It is guaranteed that given graph is a tree.

Output

Print "Yes" (without quotes), if given graph is k-multihedgehog, and "No" (without quotes) otherwise.

Examples

Input

14 2
1 4
2 4
3 4
4 13
10 5
11 5
12 5
14 5
5 13
6 7
8 6
13 6
9 6


Output

Yes


Input

3 1
1 3
2 3


Output

No

Note

2-multihedgehog from the first example looks like this:

<image>

Its center is vertex 13. Hedgehogs created on last step are: [4 (center), 1, 2, 3], [6 (center), 7, 8, 9], [5 (center), 10, 11, 12, 13].

Tree from second example is not a hedgehog because degree of center should be at least 3.
"""

from collections import deque

def is_k_multihedgehog(n, k, edges):
    G = [set() for _ in range(n + 1)]
    q, nq = deque(), deque()
    
    for u, v in edges:
        G[u].add(v)
        G[v].add(u)
    
    for u in range(1, n + 1):
        if len(G[u]) == 1:
            q.append(u)
    
    step = 0
    removed = 0
    ok = True
    
    while removed < n - 1:
        each = {}
        for u in q:
            nxt = G[u].pop()
            G[nxt].remove(u)
            each[nxt] = each.get(nxt, 0) + 1
            removed += 1
            if len(G[nxt]) == 0:
                break
            if len(G[nxt]) == 1:
                nq.append(nxt)
        
        if any(v < 3 for k, v in each.items()):
            ok = False
            break
        
        q, nq = nq, deque()
        step += 1
    
    if ok and step == k and removed == n - 1:
        return 'Yes'
    else:
        return 'No'