"""
QUESTION:
A tree of $\mbox{P}$ nodes is an un-directed connected graph having $P-1$ edges. Let us denote $\mbox{R}$ as the root node. If $\mbox{A}$ is a node such that it is at a distance of $\boldsymbol{\mbox{L}}$ from $\mbox{R}$, and $\mbox{B}$ is a node such that it is at at distance of $L+1$ from 
$\mbox{R}$ and $\mbox{A}$ is connected to $\mbox{B}$, then we call $\mbox{A}$ as the parent of $\mbox{B}$. 

Similarly, if $\mbox{A}$ is at a distance of $\boldsymbol{\mbox{L}}$ from $\mbox{R}$ and $\mbox{B}$ is at a distance of $L+K$ from $\mbox{R}$ and there is a path of length $\mbox{K}$ from $\mbox{A}$ to $\mbox{B}$, then we call $\mbox{A}$ as the $\mbox{K}^{th} $parent of $\mbox{B}$. 

Susan likes to play with graphs and Tree data structure is one of her favorites. She has designed a problem and wants to know if anyone can solve it. Sometimes she adds or removes a leaf node. Your task is to figure out the $\mbox{K}^{th} $parent of a node at any instant.

Input Format

The first line contain an integer $\mathbf{T}$ denoting the number of test cases. $\mathbf{T}$ test cases follow. First line of each test case contains an integer $\mbox{P}$, the number of nodes in the tree.
$\mbox{P}$ lines follows each containing two integers $\mbox{X}$ and $\mathbf{Y}$ separated by a single space denoting $\mathbf{Y}$ as the parent of $\mbox{X}$. If $\mathbf{Y}$ is $\mbox{0}$, then X is the root node of the tree.  ($\mbox{0}$ is for namesake and is not in the tree). 

The next line contains an integer $\mbox{Q}$, the number of queries. 

$\mbox{Q}$ lines follow each containing a query.  

$\mbox{0}$ $\mathbf{Y}$ $\mbox{X}$  : $\mbox{X}$ is added as a new leaf node whose parent is $\mathbf{Y}$ . $\mbox{X}$ is not in the tree while $\mathbf{Y}$ is in. 
$\mbox{1}$ $\mbox{X}$     : This tells that leaf node $\mbox{X}$ is removed from the tree. $\mbox{X}$ is a leaf in the tree. 
$2$ $\mbox{X}$ $\mbox{K}$   : In this query output the $\mbox{K}^{th}$ parent of $\mbox{X}$ . $\mbox{X}$ is a node in the tree. 

Note 

Each node index is any number between 1 and 10^{5} i.e., a tree with a single node can have its root indexed as 10^{5}

Constraints

$1\leq T\leq3$ 

$1\leq P\leq10^5$ 

$1\leq Q\leq10^5$ 

$1\leq X\leq10^5$ 

$\textbf{0}\leq Y\leq10^5$ 

$1\leq K\leq10^5$  

Output Format

For each query of type $2$, output the $\mbox{K}^{th} $parent of $\mbox{X}$. If $\mbox{K}^{th} $parent doesn't exist, output $\mbox{0}$ and if the node doesn't exist, output $\mbox{0}$.

Sample Input
2
7
2 0
5 2
3 5
7 5
9 8
8 2
6 8
10
0 5 15
2 15 2
1 3
0 15 20
0 20 13
2 13 4
2 13 3
2 6 10
2 11 1
2 9 1
1
10000 0
3
0 10000 4
1 4
2 4 1

Sample Output
2
2
5
0
0
8
0

Explanation

There are 2 test cases. The first test case has 7 nodes with 2 as its root. There are 10 queries

0 5 15 -> 15 is added as a leaf node to 5. 
2 15 2 -> 2nd parent of 15 is 15->5->2 is 2. 
1 3 -> leaf node 3 is removed from the tree. 
0 15 20 -> 20 is added as a leaf node to 15. 
0 20 13 -> 13 is added as a leaf node to 20.
2 13 4 -> 4th parent of 13 is 2. 
2 13 3 -> 3rd parent of 13 is 5.
2 6 10 -> there is no 10th parent of 6 and hence 0. 
2 11 1 -> 11 is not a node in the tree, hence 0.
2 9 1 -> 9's parent is 8.  

the second testcase has a tree with only 1 node (10000). 

0 10000 4 -> 4 is added as a leaf node to 10000.
1 4 -> 4 is removed. 
2 4 1 -> as 4 is already removed, answer is 0.
"""

def find_kth_parent(test_cases):
    results = []
    N = 100002
    d = [0] * N
    P = [0] * N

    def add(p, c):
        d[c] = d[p] + 1
        v = [p]
        for i in range(17):
            if not P[p] or len(P[p]) <= i:
                break
            p = P[p][i]
            v.append(p)
        P[c] = v

    for case in test_cases:
        P = [0] * N
        d = [0] * N
        edges = case['edges']
        queries = case['queries']
        R = None
        c = [[] for _ in range(N)]

        for x, y in edges:
            if y == 0:
                R = x
            else:
                c[y].append(x)

        if R is None:
            continue

        l = [R]
        while l:
            p = l.pop()
            l.extend(c[p])
            for h in c[p]:
                add(p, h)

        for query in queries:
            if query[0] == 0:
                _, Y, X = query
                add(Y, X)
            elif query[0] == 1:
                _, X = query
                d[X] = 0
            elif query[0] == 2:
                _, X, K = query
                if d[X] < K:
                    results.append(0)
                    continue
                for i in range(17):
                    if 1 << i & K:
                        X = P[X][i]
                results.append(X)

    return results