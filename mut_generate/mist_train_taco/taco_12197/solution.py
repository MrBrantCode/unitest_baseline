"""
QUESTION:
In this problem at each moment you have a set of intervals. You can move from interval (a, b) from our set to interval (c, d) from our set if and only if c < a < d or c < b < d. Also there is a path from interval I1 from our set to interval I2 from our set if there is a sequence of successive moves starting from I1 so that we can reach I2.

Your program should handle the queries of the following two types:

  1. "1 x y" (x < y) — add the new interval (x, y) to the set of intervals. The length of the new interval is guaranteed to be strictly greater than all the previous intervals.
  2. "2 a b" (a ≠ b) — answer the question: is there a path from a-th (one-based) added interval to b-th (one-based) added interval? 



Answer all the queries. Note, that initially you have an empty set of intervals.

Input

The first line of the input contains integer n denoting the number of queries, (1 ≤ n ≤ 105). Each of the following lines contains a query as described above. All numbers in the input are integers and don't exceed 109 by their absolute value.

It's guaranteed that all queries are correct.

Output

For each query of the second type print "YES" or "NO" on a separate line depending on the answer.

Examples

Input

5
1 1 5
1 5 11
2 1 2
1 2 9
2 1 2


Output

NO
YES
"""

def process_interval_queries(queries):
    def dfs(G, start, path_exists):
        s = [start]
        visited = set([])
        if not start in path_exists:
            path_exists[start] = set([])
        while s:
            node = s.pop()
            if not node in visited:
                visited.add(node)
                path_exists[start].add(node)
                (a, b) = G[node]
                for (i, (c, d)) in enumerate(G):
                    if i != node:
                        if i in path_exists[start] or c < a < d or c < b < d:
                            s.append(i)

    G = []
    path_exists = {}
    results = []

    for query in queries:
        q, a, b = query
        if q == 1:
            G.append((a, b))
        else:
            a -= 1
            b -= 1
            dfs(G, a, path_exists)
            if b in path_exists[a]:
                results.append('YES')
            else:
                results.append('NO')

    return results