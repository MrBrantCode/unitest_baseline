"""
QUESTION:
There is a tree with N vertices, numbered 1 through N. The i-th of the N-1 edges connects vertices a_i and b_i.

Currently, there are A_i stones placed on vertex i. Determine whether it is possible to remove all the stones from the vertices by repeatedly performing the following operation:

* Select a pair of different leaves. Then, remove exactly one stone from every vertex on the path between those two vertices. Here, a leaf is a vertex of the tree whose degree is 1, and the selected leaves themselves are also considered as vertices on the path connecting them.



Note that the operation cannot be performed if there is a vertex with no stone on the path.

Constraints

* 2 ≦ N ≦ 10^5
* 1 ≦ a_i,b_i ≦ N
* 0 ≦ A_i ≦ 10^9
* The given graph is a tree.

Input

The input is given from Standard Input in the following format:


N
A_1 A_2 … A_N
a_1 b_1
:
a_{N-1} b_{N-1}


Output

If it is possible to remove all the stones from the vertices, print `YES`. Otherwise, print `NO`.

Examples

Input

5
1 2 1 1 2
2 4
5 2
3 2
1 3


Output

YES


Input

3
1 2 1
1 2
2 3


Output

NO


Input

6
3 2 2 2 2 2
1 2
2 3
1 4
1 5
4 6


Output

YES
"""

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v, p, aaa, links):
    if len(links[v]) == 1:
        return aaa[v]
    children = []
    for u in links[v]:
        if u == p:
            continue
        result = dfs(u, v, aaa, links)
        if result == -1:
            return -1
        children.append(result)
    if len(children) == 1:
        if aaa[v] != children[0]:
            return -1
        return children[0]
    c_sum = sum(children)
    c_max = max(children)
    o_max = c_sum - c_max
    if o_max >= c_max:
        max_pairs = c_sum // 2
    else:
        max_pairs = o_max
    min_remain = c_sum - max_pairs
    if not min_remain <= aaa[v] <= c_sum:
        return -1
    return aaa[v] * 2 - c_sum

def can_remove_all_stones(n, aaa, edges):
    if n == 2:
        return aaa[0] == aaa[1]
    
    links = [set() for _ in range(n)]
    for (a, b) in edges:
        links[a].add(b)
        links[b].add(a)
    
    s = 0
    while len(links[s]) == 1:
        s += 1
    
    return dfs(s, -1, aaa, links) == 0