"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given a rooted tree with $N$ nodes (numbered $1$ through $N$); the root is node $1$. For each valid $i$, node $i$ has weight $w_{i}$, which is either $0$ or $1$.

We want to traverse the tree using depth first search. The order in which the nodes are visited is not uniquely defined, since we may visit the children of each node in an arbitrary order. Formally, the pseudocode of DFS-traversal is:

function DFS(node n):
	node n is visited
	for each node s (s is a son of n) in some order:
		call DFS(s)
	return
call DFS(root)

For each possible DFS-traversal of the tree, consider the sequence of weights of nodes in the order in which they are visited; each node is visited exactly once, so this sequence has length $N$. Calculate the number of inversions for each such sequence. The minimum of these numbers is the *treeversion* of our tree.

Find the treeversion of the given tree.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $w_{1}, w_{2}, \ldots, w_{N}$.
Each of the following $N-1$ lines contains two space-separated integers $x$ and $y$ denoting that nodes $x$ and $y$ are connected by an edge.

------  Output ------
For each test case, print a single line containing one integer — the treeversion of the given tree.

------  Constraints ------
$1 ≤ T ≤ 1,000$
$1 ≤ N ≤ 10^{5}$
$0 ≤ w_{i} ≤ 1$ for each valid $i$
$1 ≤ x, y ≤ N$
the graph on the input is a tree
the sum of $N$ over all test cases does not exceed $10^{6}$

------  Subtasks ------
Subtask #1 (50 points):
$1 ≤ N ≤ 1,000$
the sum of $N$ over all test cases does not exceed $10,000$

Subtask #2 (50 points): original constraints

----- Sample Input 1 ------ 
1

3

1 0 1

1 2

1 3
----- Sample Output 1 ------ 
1
"""

def calculate_treeversion(n, weights, edges):
    from collections import defaultdict
    from functools import cmp_to_key

    class SubTree:
        def __init__(self, zeros, ones, inversions):
            self.zeros = zeros
            self.ones = ones
            self.inversions = inversions

        def __str__(self):
            return '0: ' + str(self.zeros) + ' 1:' + str(self.ones) + ' Inversions:' + str(self.inversions)

    def dfs(root):
        visited[root] = True
        child = [vertex for vertex in adj[root] if not visited[vertex]]
        if len(child) == 0:
            return SubTree(weights[root] ^ 1, weights[root], 0)
        results = [dfs(i) for i in child]
        results.sort(key=cmp_to_key(lambda x, y: x.ones * y.zeros - x.zeros * y.ones))
        zeros, ones, inversions = weights[root] ^ 1, weights[root], 0
        factor = weights[root]
        for sub_tree in results:
            zeros += sub_tree.zeros
            ones += sub_tree.ones
            inversions += factor * sub_tree.zeros + sub_tree.inversions
            factor += sub_tree.ones
        return SubTree(zeros, ones, inversions)

    adj = defaultdict(list)
    for x, y in edges:
        adj[x - 1].append(y - 1)
        adj[y - 1].append(x - 1)

    visited = [False] * n
    return dfs(0).inversions