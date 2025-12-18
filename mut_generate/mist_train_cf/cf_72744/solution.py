"""
QUESTION:
Given two integers `n` and `threshold`, and an array of queries, determine for each query `[ai, bi]` if cities `ai` and `bi` are connected directly or indirectly with a path whose total weight is less than or equal to `maxWeight`. Cities with labels `x` and `y` have a road between them if they share a common divisor strictly greater than `threshold`, and the weight of the road is the greatest common divisor (GCD) of `x` and `y`. 

Constraints:
`2 <= n <= 10^4`
`0 <= threshold <= n`
`1 <= queries.length <= 10^5`
`queries[i].length == 2`
`1 <= ai, bi <= n`
`ai != bi`
`1 <= maxWeight <= 10^9`

Function name: `areConnected`
"""

def areConnected(n, threshold, queries):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootx, rooty = find(x), find(y)
        if rootx == rooty:
            return
        if rank[rootx] > rank[rooty]:
            parent[rooty] = rootx
        elif rank[rootx] < rank[rooty]:
            parent[rootx] = rooty
        else:
            parent[rooty] = rootx
            rank[rootx] += 1

    for i in range(threshold + 1, n + 1):
        for j in range(i + i, n + 1, i):
            if i * j // gcd(i, j) <= n:
                union(i, j)

    return [find(a) == find(b) for a, b in queries]