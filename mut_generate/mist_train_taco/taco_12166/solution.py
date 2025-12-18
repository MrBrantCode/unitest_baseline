"""
QUESTION:
Snuke's mother gave Snuke an undirected graph consisting of N vertices numbered 0 to N-1 and M edges. This graph was connected and contained no parallel edges or self-loops.

One day, Snuke broke this graph. Fortunately, he remembered Q clues about the graph. The i-th clue (0 \leq i \leq Q-1) is represented as integers A_i,B_i,C_i and means the following:

* If C_i=0: there was exactly one simple path (a path that never visits the same vertex twice) from Vertex A_i to B_i.
* If C_i=1: there were two or more simple paths from Vertex A_i to B_i.



Snuke is not sure if his memory is correct, and worried whether there is a graph that matches these Q clues. Determine if there exists a graph that matches Snuke's memory.

Constraints

* 2 \leq N \leq 10^5
* N-1 \leq M \leq N \times (N-1)/2
* 1 \leq Q \leq 10^5
* 0 \leq A_i,B_i \leq N-1
* A_i \neq B_i
* 0 \leq C_i \leq 1
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N M Q
A_0 B_0 C_0
A_1 B_1 C_1
\vdots
A_{Q-1} B_{Q-1} C_{Q-1}


Output

If there exists a graph that matches Snuke's memory, print `Yes`; otherwise, print `No`.

Examples

Input

5 5 3
0 1 0
1 2 1
2 3 0


Output

Yes


Input

4 4 3
0 1 0
1 2 1
2 3 0


Output

No


Input

10 9 9
7 6 0
4 5 1
9 7 0
2 9 0
2 3 0
4 1 0
8 0 0
9 1 0
3 0 0


Output

No
"""

def is_graph_possible(n, m, q, a_list, b_list, c_list):
    class UnionFind:
        def __init__(self, n):
            self.par = [i for i in range(n + 1)]
            self.rank = [0] * (n + 1)

        def find(self, x):
            if self.par[x] == x:
                return x
            else:
                self.par[x] = self.find(self.par[x])
                return self.par[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if self.rank[x] < self.rank[y]:
                self.par[x] = y
            else:
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

        def same_check(self, x, y):
            return self.find(x) == self.find(y)

    res = 'Yes'
    uf = UnionFind(n - 1)
    
    for i in range(q):
        if c_list[i] == 0:
            uf.union(a_list[i], b_list[i])
    
    for i in range(q):
        if c_list[i] == 1:
            if uf.same_check(a_list[i], b_list[i]):
                res = 'No'
    
    par_list = [0] * n
    for i in range(n):
        par_list[i] = uf.find(i)
    
    k = len(set(par_list))
    
    if max(c_list) == 0:
        min_m = n - 1
    else:
        min_m = n
    
    if m < min_m:
        res = 'No'
    elif m > n + k * (k - 3) // 2:
        res = 'No'
    
    return res