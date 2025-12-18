"""
QUESTION:
Consider an undirected graph containing $N$ nodes and $\mbox{M}$ edges. Each edge $\textit{M}_i$ has an integer cost, $C_i$, associated with it.

The penalty of a path is the bitwise OR of every edge cost in the path between a pair of nodes, $\mbox{A}$ and $\mbox{B}$. In other words, if a path contains edges $M_1,M_2,\ldots,M_k$, then the penalty for this path is $C_1$ OR $C_2$ OR ... OR $C_{k}$.

Given a graph and two nodes, $\mbox{A}$ and $\mbox{B}$, find the path between $\mbox{A}$ and $\mbox{B}$ having the minimal possible penalty and print its penalty; if no such path exists, print $-1$ to indicate that there is no path from $\mbox{A}$ to $\mbox{B}$.

Note: Loops and multiple edges are allowed. The bitwise OR operation is known as or in Pascal and as | in C++ and Java.

Input Format

The first line contains two space-separated integers, $N$ (the number of nodes) and $\mbox{M}$ (the number of edges), respectively.

Each line $\boldsymbol{i}$ of the $\mbox{M}$ subsequent lines contains three space-separated integers $U_i$, $V_i$, and $C_i$, respectively, describing edge $\textit{M}_i$ connecting the nodes $U_i$ and $V_i$ and its associated penalty ($C_i$).

The last line contains two space-separated integers, $\mbox{A}$ (the starting node) and $\mbox{B}$ (the ending node), respectively.

Constraints

$1\leq N\leq10^3$
$1\leq M\leq10^4$
$1\leq C_i<1024$
$1\leq U_i,V_i\leq N$
$1\leq A,B\leq N$
$A\neq B$

Output Format

Print the minimal penalty for the optimal path from node $\mbox{A}$ to node $\mbox{B}$; if no path exists from node $\mbox{A}$ to node $\mbox{B}$, print $-1$.

Sample Input
3 4
1 2 1
1 2 1000
2 3 3
1 3 100
1 3

Sample Output
3

Explanation

The optimal path is $1\rightarrow2\rightarrow3$. 

$C_{(1,2)}=1$ and $C_{(2,3)}=3$. 

The penalty for this path is: $1$ OR $3=3$, so we print $3$.
"""

def find_minimal_penalty(n, edges, start, end):
    # Convert 1-based node indices to 0-based for internal processing
    start -= 1
    end -= 1
    
    # Create adjacency list for the graph
    edge = [[] for _ in range(n)]
    for (u, v, cost) in edges:
        edge[u - 1].append((v - 1, cost))
        edge[v - 1].append((u - 1, cost))
    
    # Helper function to check if there's a path from start to end with given forbidden bits
    def can_reach(forbid):
        seen = [False] * n
        stack = [start]
        while stack:
            v = stack.pop()
            if v == end:
                return True
            if not seen[v]:
                seen[v] = True
                stack += [v2 for (v2, cost) in edge[v] if cost & forbid == 0]
        return False
    
    # Main logic to find the minimal penalty
    if not can_reach(0):
        return -1
    
    ans = 0
    forbid = 0
    curbit = 512
    while curbit:
        if can_reach(forbid | curbit):
            forbid |= curbit
        else:
            ans |= curbit
        curbit >>= 1
    
    return ans