"""
QUESTION:
There is a tree with N vertices numbered 1 through N. The i-th of the N-1 edges connects vertices a_i and b_i.

Initially, each edge is painted blue. Takahashi will convert this blue tree into a red tree, by performing the following operation N-1 times:

* Select a simple path that consists of only blue edges, and remove one of those edges.
* Then, span a new red edge between the two endpoints of the selected path.



His objective is to obtain a tree that has a red edge connecting vertices c_i and d_i, for each i.

Determine whether this is achievable.

Constraints

* 2 ≤ N ≤ 10^5
* 1 ≤ a_i,b_i,c_i,d_i ≤ N
* a_i ≠ b_i
* c_i ≠ d_i
* Both input graphs are trees.

Input

Input is given from Standard Input in the following format:


N
a_1 b_1
:
a_{N-1} b_{N-1}
c_1 d_1
:
c_{N-1} d_{N-1}


Output

Print `YES` if the objective is achievable; print `NO` otherwise.

Examples

Input

3
1 2
2 3
1 3
3 2


Output

YES


Input

5
1 2
2 3
3 4
4 5
3 4
2 4
1 4
1 5


Output

YES


Input

6
1 2
3 5
4 6
1 6
5 1
5 3
1 4
2 6
4 3
5 6


Output

NO
"""

import queue

def is_red_tree_achievable(N, blue_edges, red_edges):
    s = [set() for _ in range(N + 1)]
    q = queue.Queue()
    
    for u, v in blue_edges:
        if v in s[u]:
            q.put((u, v))
        else:
            s[u].add(v)
            s[v].add(u)
    
    f = [i for i in range(N + 1)]
    
    def find(x):
        if f[x] == x:
            return x
        else:
            f[x] = find(f[x])
            return f[x]
    
    while not q.empty():
        u, v = map(find, q.get())
        if u == v:
            continue
        if len(s[u]) < len(s[v]):
            u, v = v, u
        s[u].remove(v)
        s[v].remove(u)
        for x in s[v]:
            s[x].remove(v)
            if u in s[x]:
                q.put((u, x))
            else:
                s[u].add(x)
                s[x].add(u)
        s[v], f[v] = ([], u)
    
    root = find(1)
    for i in range(2, N + 1):
        if find(i) != root:
            return False
    return True