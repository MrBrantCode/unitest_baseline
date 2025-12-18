"""
QUESTION:
Create a function `numIslands2` that takes four parameters: `m` (the number of rows), `n` (the number of columns), and `positions` (a list of lists containing the row and column indices of new land cells). The function should return a list where each element `i` represents the number of islands after the `i-th` operation. The function should run in `O(k log(mn))` time complexity, where `k` is the length of `positions`. The constraints are `1 <= m, n, k <= 10^4` and `1 <= m * n <= 10^4`.
"""

def numIslands2(m, n, positions):
    parent, rank, count, res = {}, {}, 0, []
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        nonlocal count
        xr, yr = find(x), find(y)
        if xr != yr:
            if rank[xr] < rank[yr]:
                xr, yr = yr, xr
            if rank[xr] == rank[yr]:
                rank[xr] += 1
            parent[yr] = xr
            count -= 1
    for x, y in positions:
        index = x * n + y
        if index not in parent:
            parent[index] = index
            rank[index] = 0
            count += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            nindex = nx * n + ny
            if 0 <= nx < m and 0 <= ny < n and nindex in parent:
                union(index, nindex)
        res.append(count)
    return res