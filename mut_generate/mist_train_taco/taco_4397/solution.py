"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef has a tree with $N$ nodes (numbered $1$ through $N$) and a non-negative integer $x$. The nodes of the tree have non-negative integer weights; let's denote the weight of node $i$ by $a_{i}$.

Next, let's define the *XOR value* of a tree as the bitwise XOR of weights of all its nodes.

Chef wants to remove zero or more edges from his tree in such a way that each individual tree in the forest formed by removing these edges has XOR value $x$. Help him compute the number of ways to remove a set of edges such that this condition is satisfied. Since the answer may be large, compute it modulo $10^{9}+7$.

------  Input ------
The first line of the input contains two space-separated integers $N$ and $x$.
The second line contains $N$ space-separated integers $a_{1}, a_{2}, \ldots, a_{N}$.
Each of the following $N-1$ lines contains two space-separated integers $u$ and $v$ denoting an edge between nodes $u$ and $v$ in Chef's tree.

------  Output ------
Print a single line containing one integer ― the number of ways to remove edges, modulo $10^{9}+7$.

------  Constraints  ------
$1 ≤ N ≤ 10^{5}$
$0 ≤ x ≤ 10^{9}$
$0 ≤ a_{i} ≤ 10^{9}$ for each valid $i$
$1 ≤ u, v ≤ N$

------  Subtasks ------
Subtask #1 (10 points): $N ≤ 100$

Subtask #2 (20 points): $N ≤ 5,000$

Subtask #3 (70 points): original constraints

----- Sample Input 1 ------ 
7 1
1 0 1 0 1 0 1 
1 2
1 3
2 4
2 5
3 6
3 7
----- Sample Output 1 ------ 
5
----- explanation 1 ------ 
There are five valid ways to remove edges, splitting the tree into subtrees on nodes:
- [1, 2, 3, 4, 5, 6] and [7] by removing the edge (3-7)
- [1, 2, 3, 4, 6, 7] and [5] by removing the edge (2-5)
- [2, 4, 5] and [1, 3, 6, 7] by removing the edge (1-2)
- [2, 4, 5], [1], [3,6] and [7] by removing edges (1-2), (1-3) and (3-7)
- [1, 2, 4], [5], [3,6] and [7] by removing edges (2-5), (1-3) and (3-7)
"""

MOD = 10**9 + 7

def count_ways_to_remove_edges(N, x, weights, edges):
    # Build the adjacency list representation of the tree
    tree = [[] for _ in range(N)]
    for u, v in edges:
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)
    
    def dfs(i, p, x):
        Z = [[weights[i], 1]]
        Y = []
        for j in tree[i]:
            if j != p:
                Y.append(dfs(j, i, x))
        for sub in Y:
            temp = []
            for y in sub:
                for m in Z:
                    flag = True
                    flag0 = True
                    if y[0] == x:
                        for o in temp:
                            if o[0] == m[0]:
                                o[1] += y[1] * m[1]
                                flag0 = False
                        if flag0:
                            temp.append([m[0], y[1] * m[1]])
                    for o in temp:
                        if o[0] == y[0] ^ m[0]:
                            o[1] += y[1] * m[1]
                            flag = False
                            break
                    if flag:
                        temp.append([y[0] ^ m[0], y[1] * m[1]])
            Z = temp
        return Z
    
    ans = 0
    Z = dfs(0, -1, x)
    for m in Z:
        if m[0] == x:
            ans = m[1]
            break
    return ans % MOD