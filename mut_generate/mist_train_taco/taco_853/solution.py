"""
QUESTION:
Russian Translation Available

You are given a weighted graph with N vertices and M edges. Find the total weight of its maximum spanning tree.

Input

The first line contains one integer T denoting the number of test cases.
Each test case starts with a line containing 2 space-separated integer: N and M. Each of the following M lines contain description of one edge: three different space-separated integers: a,  b and c. a and b are different and from 1 to N each and denote numbers of vertices that are connected by this edge. c denotes weight of this edge.

Output

For each test case output one integer - the total weight of its maximum spanning tree.

Constraints
1 ≤ T ≤ 20
1 ≤ N ≤ 5000
1 ≤ M ≤ 100 000
1 ≤ c ≤ 10 000

SAMPLE INPUT
1
3 3
1 2 2
2 3 3
1 3 4

SAMPLE OUTPUT
7
"""

def calculate_maximum_spanning_tree_weight(test_cases):
    def root(x):
        while l1[x] != x:
            l1[x] = l1[l1[x]]
            x = l1[x]
        return x

    def union(x, y):
        p = root(x)
        q = root(y)
        l1[p] = l1[q]

    results = []

    for case in test_cases:
        N, M, edges = case
        l1 = list(range(N + 1))
        G = [(c, (a, b)) for a, b, c in edges]
        G.sort(reverse=True, key=lambda x: x[0])

        total_weight = 0
        for c, (x, y) in G:
            if root(x) != root(y):
                total_weight += c
                union(x, y)

        results.append(total_weight)

    return results