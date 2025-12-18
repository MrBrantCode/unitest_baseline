"""
QUESTION:
Let's define a forest as a non-directed acyclic graph (also without loops and parallel edges). One day Misha played with the forest consisting of n vertices. For each vertex v from 0 to n - 1 he wrote down two integers, degreev and sv, were the first integer is the number of vertices adjacent to vertex v, and the second integer is the XOR sum of the numbers of vertices adjacent to v (if there were no adjacent vertices, he wrote down 0). 

Next day Misha couldn't remember what graph he initially had. Misha has values degreev and sv left, though. Help him find the number of edges and the edges of the initial graph. It is guaranteed that there exists a forest that corresponds to the numbers written by Misha.

Input

The first line contains integer n (1 ≤ n ≤ 216), the number of vertices in the graph.

The i-th of the next lines contains numbers degreei and si (0 ≤ degreei ≤ n - 1, 0 ≤ si < 216), separated by a space.

Output

In the first line print number m, the number of edges of the graph.

Next print m lines, each containing two distinct numbers, a and b (0 ≤ a ≤ n - 1, 0 ≤ b ≤ n - 1), corresponding to edge (a, b).

Edges can be printed in any order; vertices of the edge can also be printed in any order.

Examples

Input

3
2 3
1 0
1 0


Output

2
1 0
2 0


Input

2
1 1
1 0


Output

1
0 1

Note

The XOR sum of numbers is the result of bitwise adding numbers modulo 2. This operation exists in many modern programming languages. For example, in languages C++, Java and Python it is represented as "^", and in Pascal — as "xor".
"""

def reconstruct_forest(n, degrees, ss):
    deg2vs = {}
    for i in range(n):
        if degrees[i] > 0:
            if degrees[i] not in deg2vs:
                deg2vs[degrees[i]] = set()
            deg2vs[degrees[i]].add(i)
    
    edges = []
    while len(deg2vs) != 0:
        leaves = deg2vs.pop(1, set())
        for leaf in leaves:
            if degrees[leaf] == 0:
                continue
            v = ss[leaf]
            edges.append((leaf, v))
            v_deg = degrees[v]
            if v_deg > 1:
                deg2vs[v_deg].remove(v)
                if len(deg2vs[v_deg]) == 0:
                    deg2vs.pop(v_deg)
            ss[v] = ss[v] ^ leaf
            degrees[v] -= 1
            if degrees[v] > 0:
                if degrees[v] not in deg2vs:
                    deg2vs[degrees[v]] = set()
                deg2vs[degrees[v]].add(v)
    
    return len(edges), edges