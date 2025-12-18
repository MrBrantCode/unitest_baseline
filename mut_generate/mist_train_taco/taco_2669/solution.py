"""
QUESTION:
Given is a simple undirected graph with N vertices and M edges. The i-th edge connects Vertex c_i and Vertex d_i.
Initially, Vertex i has the value a_i written on it. You want to change the values on Vertex 1, \ldots, Vertex N to b_1, \cdots, b_N, respectively, by doing the operation below zero or more times.
 - Choose an edge, and let Vertex x and Vertex y be the vertices connected by that edge. Choose one of the following and do it:
 - Decrease the value a_x by 1, and increase the value a_y by 1.
 - Increase the value a_x by 1, and decrease the value a_y by 1.
Determine whether it is possible to achieve the objective by properly doing the operation.

-----Constraints-----
 - 1 \leq N \leq 2 \times 10^5
 - 0 \leq M \leq 2 \times 10^5
 - -10^9 \leq a_i,b_i \leq 10^9
 - 1 \leq c_i,d_i \leq N
 - The given graph is simple, that is, has no self-loops and no multi-edges.
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N M
a_1 \cdots a_N
b_1 \cdots b_N
c_1 d_1
\vdots
c_M d_M

-----Output-----
Print Yes if it is possible to achieve the objective by properly doing the operation, and No otherwise.

-----Sample Input-----
3 2
1 2 3
2 2 2
1 2
2 3

-----Sample Output-----
Yes

You can achieve the objective by, for example, doing the operation as follows:
 - In the first operation, choose the edge connecting Vertex 1 and 2. Then, increase a_1 by 1 and decrease a_2 by 1.
 - In the second operation, choose the edge connecting Vertex 2 and 3. Then, increase a_2 by 1 and decrease a_3 by 1.
This sequence of operations makes a_1=2, a_2=2, and a_3=2.
"""

def can_transform_values(N, M, a, b, edges):
    from collections import deque
    
    # Create adjacency list for the graph
    li = [[] for _ in range(N + 1)]
    for c, d in edges:
        li[c].append(d)
        li[d].append(c)
    
    # Initialize visited array
    li2 = [0] * (N + 1)
    num = 0
    
    # Perform BFS to find connected components
    for i in range(1, N + 1):
        if li2[i] != 0:
            continue
        num += 1
        deque = [i]
        li2[i] = num
        while deque:
            x = deque.pop(0)
            for j in li[x]:
                if li2[j] == 0:
                    li2[j] = num
                    deque.append(j)
    
    # Group vertices by their connected components
    li3 = [[] for _ in range(num)]
    for i in range(1, N + 1):
        li3[li2[i] - 1].append(i - 1)
    
    # Check if the sum of values in each connected component matches
    for i in range(len(li3)):
        A = sum(a[j] for j in li3[i])
        B = sum(b[j] for j in li3[i])
        if A != B:
            return False
    
    return True