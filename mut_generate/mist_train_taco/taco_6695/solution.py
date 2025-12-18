"""
QUESTION:
Let N be an even number.
There is a tree with N vertices.
The vertices are numbered 1, 2, ..., N.
For each i (1 \leq i \leq N - 1), the i-th edge connects Vertex x_i and y_i.
Snuke would like to decorate the tree with ribbons, as follows.
First, he will divide the N vertices into N / 2 pairs.
Here, each vertex must belong to exactly one pair.
Then, for each pair (u, v), put a ribbon through all the edges contained in the shortest path between u and v.
Snuke is trying to divide the vertices into pairs so that the following condition is satisfied: "for every edge, there is at least one ribbon going through it."
How many ways are there to divide the vertices into pairs, satisfying this condition?
Find the count modulo 10^9 + 7.
Here, two ways to divide the vertices into pairs are considered different when there is a pair that is contained in one of the two ways but not in the other.

-----Constraints-----
 - N is an even number.
 - 2 \leq N \leq 5000
 - 1 \leq x_i, y_i \leq N
 - The given graph is a tree.

-----Input-----
Input is given from Standard Input in the following format:
N
x_1 y_1
x_2 y_2
:
x_{N - 1} y_{N - 1}

-----Output-----
Print the number of the ways to divide the vertices into pairs, satisfying the condition, modulo 10^9 + 7.

-----Sample Input-----
4
1 2
2 3
3 4

-----Sample Output-----
2

There are three possible ways to divide the vertices into pairs, as shown below, and two satisfy the condition: the middle one and the right one.
"""

import sys
import numpy as np

MOD = 10 ** 9 + 7

def count_valid_pairings(N, edges):
    graph = [[] for _ in range(N + 1)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def dp_merge(data1, data2):
        N1 = len(data1) - 1
        N2 = len(data2) - 1
        if N1 > N2:
            N1, N2 = N2, N1
            data1, data2 = data2, data1
        data = np.zeros(N1 + N2, dtype=np.int64)
        for n in range(1, N1 + 1):
            data[n:n + N2] += data1[n] * data2[1:] % MOD
        data %= MOD
        return data

    fact_2 = [1, 0, 1]
    for n in range(3, N + 10):
        fact_2.append(fact_2[n - 2] * (n - 1) % MOD)
    fact_2 = np.array(fact_2, dtype=np.int64)

    def dp_add_edge(data):
        N = len(data) - 1
        data1 = np.zeros(N + 2, dtype=np.int64)
        data1[1:] = data
        data1[1] = -(data * fact_2[:N + 1] % MOD).sum() % MOD
        return data1

    def dfs(v, parent=None):
        data = None
        for y in graph[v]:
            if y == parent:
                continue
            data1 = dfs(y, v)
            data1 = dp_add_edge(data1)
            if data is None:
                data = data1
            else:
                data = dp_merge(data, data1)
        if data is None:
            return np.array([0, 1], dtype=np.int64)
        return data

    data = dfs(1)
    answer = (data * fact_2[:N + 1] % MOD).sum() % MOD
    return answer