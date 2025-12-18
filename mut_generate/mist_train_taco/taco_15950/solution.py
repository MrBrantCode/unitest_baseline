"""
QUESTION:
After the piece of a devilish mirror hit the Kay's eye, he is no longer interested in the beauty of the roses. Now he likes to watch snowflakes.

Once upon a time, he found a huge snowflake that has a form of the tree (connected acyclic graph) consisting of n nodes. The root of tree has index 1. Kay is very interested in the structure of this tree.

After doing some research he formed q queries he is interested in. The i-th query asks to find a centroid of the subtree of the node vi. Your goal is to answer all queries.

Subtree of a node is a part of tree consisting of this node and all it's descendants (direct or not). In other words, subtree of node v is formed by nodes u, such that node v is present on the path from u to root.

Centroid of a tree (or a subtree) is a node, such that if we erase it from the tree, the maximum size of the connected component will be at least two times smaller than the size of the initial tree (or a subtree).

Input

The first line of the input contains two integers n and q (2 ≤ n ≤ 300 000, 1 ≤ q ≤ 300 000) — the size of the initial tree and the number of queries respectively.

The second line contains n - 1 integer p2, p3, ..., pn (1 ≤ pi ≤ n) — the indices of the parents of the nodes from 2 to n. Node 1 is a root of the tree. It's guaranteed that pi define a correct tree.

Each of the following q lines contain a single integer vi (1 ≤ vi ≤ n) — the index of the node, that define the subtree, for which we want to find a centroid.

Output

For each query print the index of a centroid of the corresponding subtree. If there are many suitable nodes, print any of them. It's guaranteed, that each subtree has at least one centroid.

Example

Input

7 4
1 1 3 3 5 3
1
2
3
5


Output

3
2
3
6

Note

<image>

The first query asks for a centroid of the whole tree — this is node 3. If we delete node 3 the tree will split in four components, two of size 1 and two of size 2.

The subtree of the second node consists of this node only, so the answer is 2.

Node 3 is centroid of its own subtree.

The centroids of the subtree of the node 5 are nodes 5 and 6 — both answers are considered correct.
"""

import bisect

def find_centroids(n, q, parents, queries):
    childs = [[] for _ in range(n)]
    for c, pa in enumerate(parents):
        childs[pa - 1].append(c + 1)
    
    toposort = []
    this_level = [0]
    next_level = []
    while len(this_level) > 0:
        for this_n in this_level:
            toposort.append(this_n)
            for c in childs[this_n]:
                next_level.append(c)
        this_level = next_level
        next_level = []
    
    sz = [0] * n
    potentials = [0] * n
    potential_sz = [0] * n
    potential_lo = [0] * n
    centr = [0] * n
    
    for node in reversed(toposort):
        if len(childs[node]) == 0:
            centr[node] = node
            sz[node] = 1
        else:
            s = 1
            lg_c = -1
            lg_c_sz = 0
            for c in childs[node]:
                s += sz[c]
                if sz[c] > lg_c_sz:
                    lg_c_sz = sz[c]
                    lg_c = c
            sz[node] = s
            if lg_c_sz <= sz[node] // 2:
                centr[node] = node
                potentials[node] = [node]
                potential_sz[node] = [sz[node]]
                continue
            potentials[node] = potentials[lg_c]
            potential_sz[node] = potential_sz[lg_c]
            i = bisect.bisect_right(potential_sz[node], sz[node] // 2, lo=potential_lo[lg_c])
            centr[node] = potentials[node][i]
            potentials[node].append(node)
            potential_lo[node] = i
            potential_sz[node].append(sz[node])
    
    results = [centr[v - 1] + 1 for v in queries]
    return results