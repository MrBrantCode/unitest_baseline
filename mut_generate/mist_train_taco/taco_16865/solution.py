"""
QUESTION:
Chinese Version

Russian Version

You are given a tree with N nodes and each has a value associated with it. You are given Q queries, each of which is either an update or a retrieval operation. 

The update query is of the format

i j X

This means you'd have to add a GP series to the nodes which lie in the path from node i to node j (both inclusive) with first term of the GP as X on node i and the common ratio as R (given in the input)

The retrieval query is of the format

i j

You need to return the sum of the node values (S) lying in the path from node i to node j modulo 100711433. 

Input Format 

The first line contains two integers (N and R respectively) separated by a space. 

In the next N-1 lines, the$ i^{th}$ line describes the $i^{th} $edge: a line with two integers a b separated by a single space denotes an edge between a, b. 

The next line contains 2 space separated integers (U and Q respectively) representing the number of Update and Query operations to follow. 

U lines follow. Each of the next U lines contains 3 space separated integers (i,j, and X respectively). 

Each of the next Q lines contains 2 space separated integers, i and j respectively. 

Output Format 

It contains exactly Q lines and each line containing the answer of the$ i^{th}$ query.

Constraints

2 <= N <= 100000 

2 <= R <= $10^{9}$ 

1 <= U <= 100000 

1 <= Q <= 100000 

1 <= X <= 10 

1 <= a, b, i, j <= N  

Sample Input  

6 2
1 2
1 4
2 6
4 5
4 3
2 2
1 6 3
5 3 5
6 4
5 1

Sample Output

31
18

Explanation

The node values after the first updation becomes :  

3 6 0 0 0 12  

The node values after second updation becomes :  

3 6 20 10 5 12  

Answer to Query #1: 12 + 6 + 3 + 10 = 31 

Answer to Query #2: 5 + 10 +3 = 18
"""

def process_tree_queries(n, r, edges, updates, queries):
    class Node:
        def __init__(self, data):
            self.data = data
            self.neighbors = []

        def add(self, neighbor):
            self.neighbors.append(neighbor)

    def path(a, b):
        s = set()
        q = [[b]]
        s.add(b)
        i = 0
        while i < len(q):
            p = q[i]
            if p[0] == a:
                return p
            for n in nodes[p[0]].neighbors:
                if n not in s:
                    s.add(n)
                    q.append([n] + p)
            i += 1
        raise Exception("Path not found")

    nodes = [Node(0) for _ in range(n)]
    for a, b in edges:
        nodes[a - 1].add(b - 1)
        nodes[b - 1].add(a - 1)

    for i, j, x in updates:
        for node_index in path(i - 1, j - 1):
            node = nodes[node_index]
            node.data += x
            x *= r

    results = []
    for i, j in queries:
        results.append(sum((nodes[node].data for node in path(i - 1, j - 1))) % 100711433)

    return results