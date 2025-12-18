"""
QUESTION:
Problem Statement

You are given a connected undirected graph which has even numbers of nodes. A connected graph is a graph in which all nodes are connected directly or indirectly by edges.

Your task is to find a spanning tree whose median value of edges' costs is minimum. A spanning tree of a graph means that a tree which contains all nodes of the graph.



Input

The input consists of multiple datasets.

The format of each dataset is as follows.


n m
s_1 t_1 c_1
...
s_m t_m c_m


The first line contains an even number n (2 \leq n \leq 1,000) and an integer m (n-1 \leq m \leq 10,000). n is the nubmer of nodes and m is the number of edges in the graph.

Then m lines follow, each of which contains s_i (1 \leq s_i \leq n), t_i (1 \leq s_i \leq n, t_i \neq s_i) and c_i (1 \leq c_i \leq 1,000). This means there is an edge between the nodes s_i and t_i and its cost is c_i. There is no more than one edge which connects s_i and t_i.

The input terminates when n=0 and m=0. Your program must not output anything for this case.

Output

Print the median value in a line for each dataset.

Example

Input

2 1
1 2 5
4 6
1 2 1
1 3 2
1 4 3
2 3 4
2 4 5
3 4 6
8 17
1 4 767
3 1 609
8 3 426
6 5 972
8 1 607
6 4 51
5 1 683
3 6 451
3 4 630
8 7 912
3 7 43
4 7 421
3 5 582
8 4 538
5 7 832
1 6 345
8 2 608
0 0


Output

5
2
421
"""

def find_minimum_median_spanning_tree(n, m, edges):
    class UnionFind:
        def __init__(self, size):
            self.table = [-1 for _ in range(size)]

        def find(self, x):
            if self.table[x] < 0:
                return x
            else:
                self.table[x] = self.find(self.table[x])
                return self.table[x]

        def union(self, x, y):
            s1 = self.find(x)
            s2 = self.find(y)
            if s1 != s2:
                if self.table[s1] <= self.table[s2]:
                    self.table[s1] += self.table[s2]
                    self.table[s2] = s1
                else:
                    self.table[s2] += self.table[s1]
                    self.table[s1] = s2
                return True
            return False

    # Sort edges by cost in ascending order
    sorted_edges = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(n + 1)
    edge_count = 0
    selected_edges = []

    # Kruskal's algorithm to find the minimum spanning tree
    for (s, t, c) in sorted_edges:
        if uf.union(s, t):
            selected_edges.append(c)
            edge_count += 1
            if edge_count == n - 1:
                break

    # Calculate the median of the selected edges' costs
    selected_edges.sort()
    median_index = (n - 1) // 2
    median_value = selected_edges[median_index]

    return median_value