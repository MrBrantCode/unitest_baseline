"""
QUESTION:
We had a really tough time generating tests for problem D. In order to prepare strong tests, we had to solve the following problem.

Given an undirected labeled tree consisting of n vertices, find a set of segments such that:

  1. both endpoints of each segment are integers from 1 to 2n, and each integer from 1 to 2n should appear as an endpoint of exactly one segment; 
  2. all segments are non-degenerate; 
  3. for each pair (i, j) such that i ≠ j, i ∈ [1, n] and j ∈ [1, n], the vertices i and j are connected with an edge if and only if the segments i and j intersect, but neither segment i is fully contained in segment j, nor segment j is fully contained in segment i. 



Can you solve this problem too?

Input

The first line contains one integer n (1 ≤ n ≤ 5 ⋅ 10^5) — the number of vertices in the tree.

Then n - 1 lines follow, each containing two integers x_i and y_i (1 ≤ x_i, y_i ≤ n, x_i ≠ y_i) denoting the endpoints of the i-th edge.

It is guaranteed that the given graph is a tree.

Output

Print n pairs of integers, the i-th pair should contain two integers l_i and r_i (1 ≤ l_i < r_i ≤ 2n) — the endpoints of the i-th segment. All 2n integers you print should be unique.

It is guaranteed that the answer always exists.

Examples

Input


6
1 2
1 3
3 4
3 5
2 6


Output


9 12
7 10
3 11
1 5
2 4
6 8


Input


1


Output


1 2
"""

def generate_segments(n, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    st = [1]
    seen = [0] * (n + 1)
    seen[1] = 1
    
    LL = [0] * (2 * n + 3)
    LL[-1] = 1
    LL[1] = 0
    
    LL_rev = [0] * (2 * n + 3)
    LL_rev[1] = -1
    LL_rev[-1] = 0
    
    st_append = st.append
    
    while st:
        v = st.pop()
        for u in adj[v]:
            if not seen[u]:
                seen[u] = 1
                st_append(u)
                v_next = LL[v]
                v_prev = LL_rev[v]
                LL[v] = u
                LL[u] = v_next
                LL_rev[v_next] = u
                LL_rev[u] = v
                u_ = -u
                LL_rev[v] = u_
                LL[v_prev] = u_
                LL[u_] = v
    
    s = -1
    ans1 = [0] * (n + 1)
    ans2 = [0] * (n + 1)
    
    for i in range(1, 2 * n + 1):
        if s < 0:
            ans1[-s] = i
        else:
            ans2[s] = i
        s = LL[s]
    
    segments = [(ans1[i], ans2[i]) for i in range(1, n + 1)]
    return segments