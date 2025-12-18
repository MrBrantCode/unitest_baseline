"""
QUESTION:
Gildong was hiking a mountain, walking by millions of trees. Inspired by them, he suddenly came up with an interesting idea for trees in data structures: What if we add another edge in a tree?

Then he found that such tree-like graphs are called 1-trees. Since Gildong was bored of solving too many tree problems, he wanted to see if similar techniques in trees can be used in 1-trees as well. Instead of solving it by himself, he's going to test you by providing queries on 1-trees.

First, he'll provide you a tree (not 1-tree) with $n$ vertices, then he will ask you $q$ queries. Each query contains $5$ integers: $x$, $y$, $a$, $b$, and $k$. This means you're asked to determine if there exists a path from vertex $a$ to $b$ that contains exactly $k$ edges after adding a bidirectional edge between vertices $x$ and $y$. A path can contain the same vertices and same edges multiple times. All queries are independent of each other; i.e. the added edge in a query is removed in the next query.


-----Input-----

The first line contains an integer $n$ ($3 \le n \le 10^5$), the number of vertices of the tree.

Next $n-1$ lines contain two integers $u$ and $v$ ($1 \le u,v \le n$, $u \ne v$) each, which means there is an edge between vertex $u$ and $v$. All edges are bidirectional and distinct.

Next line contains an integer $q$ ($1 \le q \le 10^5$), the number of queries Gildong wants to ask.

Next $q$ lines contain five integers $x$, $y$, $a$, $b$, and $k$ each ($1 \le x,y,a,b \le n$, $x \ne y$, $1 \le k \le 10^9$) – the integers explained in the description. It is guaranteed that the edge between $x$ and $y$ does not exist in the original tree.


-----Output-----

For each query, print "YES" if there exists a path that contains exactly $k$ edges from vertex $a$ to $b$ after adding an edge between vertices $x$ and $y$. Otherwise, print "NO".

You can print each letter in any case (upper or lower).


-----Example-----
Input
5
1 2
2 3
3 4
4 5
5
1 3 1 2 2
1 4 1 3 2
1 4 1 3 3
4 2 3 3 9
5 2 3 3 9

Output
YES
YES
NO
YES
NO



-----Note-----

The image below describes the tree (circles and solid lines) and the added edges for each query (dotted lines). [Image] 

Possible paths for the queries with "YES" answers are:   $1$-st query: $1$ – $3$ – $2$  $2$-nd query: $1$ – $2$ – $3$  $4$-th query: $3$ – $4$ – $2$ – $3$ – $4$ – $2$ – $3$ – $4$ – $2$ – $3$
"""

from collections import namedtuple
from sys import stdin, stderr

Path = namedtuple('Path', 'length midlength middle left right')

def can_reach_in_k_steps(n, edges, queries):
    adj = [[] for _ in range(n + 1)]
    paths = [None for _ in range(n + 1)]
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    def append(path, x):
        if not path:
            return Path(1, 1, x, None, None)
        l = path.length + 1
        if l >= 2 * path.midlength:
            return Path(l, path.midlength * 2, x, path, None)
        else:
            return Path(l, path.midlength, path.middle, path.left, append(path.right, x))
    
    queue = [(1, 0)]
    for i in range(n):
        v, parent = queue[i]
        paths[v] = append(paths[parent], v)
        for u in adj[v]:
            if u != parent:
                queue.append((u, v))
    
    def gcp(x, y):
        if not x or not y:
            return 0
        while x.midlength > y.midlength:
            x = x.left
        while y.midlength > x.midlength:
            y = y.left
        if x.middle == y.middle:
            return x.midlength + gcp(x.right, y.right)
        else:
            return gcp(x.left, y.left)
    
    def dist(x, y):
        px = paths[x]
        py = paths[y]
        return px.length + py.length - 2 * gcp(px, py)
    
    results = []
    for x, y, a, b, k in queries:
        ds = [dist(a, b), dist(a, x) + 1 + dist(y, b), dist(a, y) + 1 + dist(x, b)]
        for d in ds:
            if k >= d and (k - d) % 2 == 0:
                results.append("YES")
                break
        else:
            results.append("NO")
    
    return results