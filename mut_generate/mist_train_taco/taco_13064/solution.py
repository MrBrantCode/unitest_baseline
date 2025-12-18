"""
QUESTION:
You are given a graph with n vertices and m edges.
You can remove one edge from anywhere and add that edge between any two vertices in one operation.
Find the minimum number of operation that will be required to make the graph connected.
If it is not possible to make the graph connected, return -1.
 
Example 1: 
Input:
n=4
m=3
Edge=[ [0, 1] , [0, 2] , [1, 2] ]
Output:
1
Explanation:
Remove edge between vertices 1 and 2 and add between vertices 1 and 3.
 
Example 2:
Input:
n=6
m=5
Edge=[ [0,1] , [0,2] , [0,3] , [1,2] , [1,3] ]
Output:
2
Explanation:
Remove edge between (1,2) and(0,3) and add edge between (1,4) and (3,5)
 
 
Your Task:
You don't need to read or print anything. Your task is to complete the function Solve() which takes an integer n denoting no. of vertices and a matrix edge[][] denoting the the edges of graph and return the minimum number of operation to connect a graph
 
Constraints:
1<=n<=10^{5}
0<=m<=10^{5}
0<=edge[i][0],edge[i][1]
"""

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def union(self, a, b):
        (a, b) = (self.find(a), self.find(b))
        if a == b:
            return
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        elif self.rank[b] > self.rank[a]:
            (a, b) = (b, a)
        self.parent[b] = a

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

def min_operations_to_connect_graph(n, edges):
    ds = UnionFind()
    cntExtras = 0
    for u, v in edges:
        if ds.find(u) == ds.find(v):
            cntExtras += 1
        else:
            ds.union(u, v)
    cntComps = sum(1 for i in range(n) if ds.find(i) == i)
    ans = cntComps - 1
    if cntExtras >= ans:
        return ans
    else:
        return -1