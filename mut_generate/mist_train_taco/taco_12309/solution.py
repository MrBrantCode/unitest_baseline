"""
QUESTION:
You are given a Directed Acyclic Graph (DAG) with $n$ vertices and $m$ edges. Each vertex $v$ has an integer, $a_v$, associated with it and the initial value of $a_v$ is $0$ for all vertices. You must perform $\textit{q}$ queries on the DAG, where each query is one of the following types:

1 u x: Set $a_v$ to $\boldsymbol{x}$ for all $v$ such that there is a path in the DAG from $\mbox{u}$ to $v$.
2 u x: Set $a_v$ to $\boldsymbol{x}$ for all $v$ such that there is a path from $\mbox{u}$ to $v$ and $a_v>x$.
3 u: Print the value of $a_{u}$ on a new line.

Input Format

The first line contains three space-separated integers describing the respective values of $n$ (the number of vertices in the DAG), $m$ (the number of edges in the DAG), and $\textit{q}$ (the number of queries to perform). 

Each of the $m$ subsequent lines contains two space-separated integers describing the respective values of $\mbox{u}$ and $v$ (where $1\leq u,v\leq n$, $u\neq v$) denoting a directed edge from vertex $\mbox{u}$ to vertex $v$ in the graph. 

Each of the $\textit{q}$ subsequent lines contains a query in one of the three formats described above.

Constraints

$2\leq n\leq10^5$
$1\leq m,q\leq10^5$
$0\leq x\leq10^9$
$0\leq a_v\leq10^9$
It's guaranteed that the graph is acyclic, but there may be more than one edge connecting two nodes.

Output Format

For each query of type $3$ (i.e., 3 u), print the value of $a_{u}$ on a new line.

Sample Input 0
6 5 18
1 2
1 3
3 4
2 4
5 6
1 1 3
3 1
3 2
3 3
3 4
1 2 2
3 1
3 2
3 3
3 4
2 6 7
3 5
3 6
2 1 3
3 1
3 2
3 3
3 4

Sample Output 0
3
3
3
3
3
2
3
2
0
0
3
2
3
2

Explanation 0

The diagram below depicts the changes to the graph after all type $1$ and type $2$ queries:
"""

from functools import reduce

def process_dag_queries(n, m, q, edges, queries):
    vertexes = [0] * (n + 1)
    
    def memoize(f):
        cache = {}
        def ret(n):
            if n not in cache:
                cache[n] = f(n)
            return cache[n]
        return ret

    @memoize
    def reachable(n):
        return reduce(lambda x, y: x | y, (reachable(it) for it in edges[n]), {n})
    
    results = []
    
    for query in queries:
        if query[0] == 1:
            for it in reachable(query[1]):
                vertexes[it] = query[2]
        elif query[0] == 2:
            for it in reachable(query[1]):
                vertexes[it] = min(vertexes[it], query[2])
        elif query[0] == 3:
            results.append(vertexes[query[1]])
    
    return results